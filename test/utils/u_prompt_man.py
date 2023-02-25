#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 19:22
# @Author  : Samge
import random

from test.utils import u_log

# <lora:koreanDollLikeness_v10:0.3>,
# <lora:taiwanDollLikeness_v10:0.2>
# <lora:japaneseDollLikeness_v10:0.2>
# <lora:asiangirllikeness_v10:0.1>
# <lora:artErosAerosATribute_aerosNovae:0.1>
# <lora:evoart_v20:0.1>
# <lora:pureerosface_v1:0.1>"


scenery_descriptions_top30_man = ["Boardroom meeting", "Power lunch", "Golf course", "Tennis court", "Ski resort", "Private jet", "Luxury yacht", "Exclusive club", "Fine dining restaurant", "Wine tasting event", "Art gallery opening", "Opera house", "Symphony hall", "Charity gala", "Red carpet event", "Fashion show", "Movie premiere", "VIP lounge", "High-end casino", "Private party", "Business conference", "CEO summit", "Investment seminar", "Luxury car dealership", "Private gym", "Polo match", "Sailing regatta", "Horse racing", "Formula One race", "Private island retreat"]
clothing_descriptions_man = ["Suit", "Tuxedo", "Blazer", "Dress shirt", "Polo shirt", "Henley shirt", "Button-down shirt", "Dress pants", "Chinos", "Khakis", "Jeans", "Bomber jacket", "Leather jacket", "Denim jacket", "Trench coat", "Peacoat", "Overcoat", "Parka", "Hoodie", "Cardigan", "V-neck sweater", "Crew-neck sweater", "Scarf", "Tie", "Bow tie", "Pocket square", "Cufflinks", "Loafers", "Dress shoes", "Sneakers"]
time_descriptions = [    "10:00 AM",    "2:30 PM",    "7:15 AM",    "11:45 PM",    "6:00 PM",    "9:30 AM",    "3:45 PM",    "8:00 AM",    "1:00 PM",    "5:30 PM",    "12:15 PM",    "4:45 AM",    "11:00 PM",    "8:30 AM",    "2:00 PM",    "6:30 PM",    "10:45 AM",    "12:00 PM",    "7:00 PM",    "9:00 AM"]
posture_verbs = ['Crew Cut', 'Ivy League Cut', 'High and Tight', 'Slicked Back', 'Side Part', 'Undercut', 'French Crop', 'Buzz Cut', 'Textured Crop', 'Pompadour']


def get_scenery() -> str:
    return random.choice(scenery_descriptions_top30_man)


def get_clothing() -> str:
    return random.choice(clothing_descriptions_man)


def get_time() -> str:
    # return random.choice(time_descriptions)
    return 'night'


def get_posture() -> str:
    return random.choice(posture_verbs)


def get_lora() -> str:
    default_lora = "<lora:koreanDollLikeness_v10:0.5>,<lora:taiwanDollLikeness_v10:0.2>,<lora:patrickBatemanChristian_patrickBatemanV1:0.1>"
    num = random.choice([0.0, 0.1, 0.2])
    if num == 0:
        return default_lora
    return f"{default_lora},<lora:japaneseDollLikeness_v10:{num}>"


def get_negative_prompt() -> str:
    return "EasyNegative, paintings, sketches, (worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, age spot, glans,extra fingers,fewer fingers,((watermark:2)),((white letters:1))"


def get_prompt() -> str:
    return get_prompt_dict().get('prompt')


def get_prompt_dict() -> dict:
    scenery = get_scenery()
    clothing = get_clothing()
    _time = get_time()
    posture = get_posture()
    lora = get_lora()
    u_log.print_log(f"当前获取的随机参数：场景：{scenery}， 服装：{clothing}， 时间：{_time}， 发型：{posture}， lora：{lora}")
    prompt = f"{lora}(8k, RAW photo, best quality, masterpiece:1.2), (realistic, photo-realistic:1.37), ultra-detailed, 1 girl,cute, solo,beautiful detailed sky,background {scenery},{_time},{posture},dating,(nose blush),(smile:1.1),(closed mouth) medium breasts,beautiful detailed eyes,({clothing}:1.1), bowtie,pleated skirt,(short hair:1.2),floating hair"
    prompt = f"{lora}(8k, RAW photo, best quality, masterpiece:1.2), (realistic, photo-realistic:1.5), ultra-detailed,background {scenery},{_time}, 1 man, handsome with an Asian facial structure,{posture}, small and well-defined features, delicate and refined appearance, wearing a casual suit with a weight of 1.1, standing on the street with a relaxed and confident demeanor, exuding an air of sophistication and charm, clean-shaven with a focus on his chiseled jawline and defined cheekbones, with his hair styled to perfection, capturing his suave and stylish personality with a touch of raw masculinity."
    return {
        'scenery': scenery,
        'clothing': clothing,
        'time': _time,
        'posture': posture,
        'prompt': prompt,
    }


def get_batch_size() -> int:
    """获取每次生成多少张图，默认1，显卡的显存够的话可以调整多些"""
    lst = [1, 2, 4, 8]
    return random.choice(lst)
    # return 1


def get_steps() -> int:
    lst = [30, 50, 60, 80, 90, 130]
    return random.choice(lst)


def get_cfg_scale() -> float:
    return round(random.uniform(7.0, 7.6), 1)


def get_sampler_name() -> str:
    return 'DPM++ 2M Karras'


def get_sd_model_checkpoint() -> str:
    return "chilloutmix_NiPrunedFp32Fix"


def get_width_height() -> (int, int):
    return 768, 1280


def get_seed() -> int:
    return -1


def get_config() -> dict:
    sampler_name = get_sampler_name()
    width, height = get_width_height()
    prompt_dict = get_prompt_dict()
    return {
      "prompt": prompt_dict.get('prompt'),
      "sampler_name": sampler_name,
      "batch_size": get_batch_size(),
      "steps": get_steps(),
      "cfg_scale": get_cfg_scale(),
      "width": width,
      "height": height,
      "negative_prompt": get_negative_prompt(),
      "sampler_index": sampler_name,
      "sd_model_checkpoint": get_sd_model_checkpoint(),
      "seed": get_seed(),
      "prompt_dict": prompt_dict
    }


if __name__ == '__main__':
    # print(get_cfg_scale())
    # for k,v in get_config().items():
    #     print(f"{k}: {v}")
    print(get_clothing())
