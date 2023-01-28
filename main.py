import functions_framework
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline, LMSDiscreteScheduler
import base64
from io import BytesIO
import os
import file_utils
import storage_utils
from model_utils import check_or_download_model
from date_utils import print_with_date
from data_utils import get_json_request_data
import check_gpu as cg

@functions_framework.http
def inference(request):
    request_json = request.get_json(silent=True)
    
    print("inference call started")
    check_or_download_model(request_json)
    # return {'status':'success'}
    
    global model
    model = StableDiffusionPipeline.from_pretrained("model")#.to("cuda")

    prompt = request_json['prompt'] if request_json and 'prompt' in request_json else "Super mario flying to the moon"
    height = request_json['height'] if request_json and 'height' in request_json else 512
    width = request_json['width'] if request_json and 'width' in request_json else 512
    num_inference_steps = request_json['num_inference_steps'] if request_json and 'num_inference_steps' in request_json else 1#50
    guidance_scale = request_json['guidance_scale'] if request_json and 'guidance_scale' in request_json else 7.5
    input_seed = request_json["seed"] if request_json and 'seed' in request_json else None

    #If "seed" is not sent, we won't specify a seed in the call
    generator = None
    if input_seed != None:
        generator = torch.Generator("cuda").manual_seed(input_seed)
    
    if prompt == None:
        return {'message': "No prompt provided"}
    
    # Run the model
    with autocast("cuda"):
        image = model(prompt,height=height,width=width,num_inference_steps=num_inference_steps,guidance_scale=guidance_scale,generator=generator)["images"][0]
    
    buffered = BytesIO()
    image.save(buffered,format="JPEG")
    image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

    # Return the results as a dictionary
    return {'image_base64': image_base64}


@functions_framework.http
def check_gpu(request):
    return cg.has_nvidia_drivers()