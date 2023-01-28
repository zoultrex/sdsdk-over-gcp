import torch
from torch import autocast
from diffusers import StableDiffusionPipeline, LMSDiscreteScheduler
import base64
from io import BytesIO
import os


HF_AUTH_TOKEN = "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"
global model
# model = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5",use_auth_token=HF_AUTH_TOKEN).to("cuda")
model = StableDiffusionPipeline.from_pretrained("model")

# pipe.safety_checker = lambda images, **kwargs: (images, False)
def dummy(images, **kwargs):
    return images, False
model.safety_checker = dummy

prompt = "a boat made of crystal in a rainbow river, floating in a distant galaxy"
height = 512
width = 512
num_inference_steps = 1#50
guidance_scale = 7.5
input_seed = None
generator = None
# generator = torch.Generator("cuda").manual_seed(input_seed)

# Run the model
with autocast("cuda"):
    image = model(prompt,height=height,width=width,num_inference_steps=num_inference_steps,guidance_scale=guidance_scale,generator=generator)["images"][0]

# print(image)
buffered = BytesIO()
image.save(buffered,format="JPEG")
image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
print(image_base64)
print("finished inference")