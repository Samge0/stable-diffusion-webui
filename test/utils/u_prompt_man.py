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

# scenery_descriptions_new2 = ["星巴克咖啡店", "香港街头", "香港太平山上", "深圳海边", "深圳平安大厦", "深圳梧桐山", "音乐厅", "电影院", "麦当劳店里", "肯德基店里", "古风小巷", "福建鼓浪屿", "飞龙雪山", "西藏", "青海湖", "夏威夷海边", "城中村"]
scenery_descriptions_new2 = ["Starbucks coffee shop", "Hong Kong street", "Victoria Peak in Hong Kong", "Beach in Shenzhen", "Ping An Finance Center in Shenzhen", "Wutong Mountain in Shenzhen", "Concert hall", "Movie theater", "Inside McDonald's", "Inside KFC", "Ancient-style alley", "Gulangyu Island in Fujian", "Jade Dragon Snow Mountain", "Tibet", "Qinghai Lake", "Beach in Hawaii", "Urban village"]

scenery_descriptions_new = ["detailed cafe", "Botanical Garden", "Rooftop bar", "Hot air balloon ride", "Beach picnic", "Art museum", "Winery tour", "Romantic restaurant", "Horse-drawn carriage ride", "Sunset cruise", "Candlelit concert", "Ice skating rink", "Fancy cocktail bar", "Opera house", "Boutique hotel", "Nature hike", "Champagne brunch", "Cooking class", "Drive-in movie theater", "Aquarium", "Dinner theater", "Scenic train ride", "Salsa dancing class", "Vintage flea market", "Roller skating rink", "Mansion tour", "Amusement park", "Poetry reading", "Sushi-making class", "Street festival", "Ballet performance", "detailed cafe"]
scenery_descriptions_top30_world = ["The Great Wall of China", "Machu Picchu", "Taj Mahal", "Petra", "Angkor Wat", "The Colosseum", "The Grand Canyon", "Niagara Falls", "Santorini", "The Pyramids of Giza", "The Acropolis of Athens", "The Eiffel Tower", "The Statue of Liberty", "The Grand Palace", "Stonehenge", "The Vatican City", "The Parthenon", "The Christ the Redeemer Statue", "The Alhambra", "The Sagrada Familia", "The Great Barrier Reef", "The Sydney Opera House", "The Tower Bridge", "The Big Ben", "The Palace of Versailles", "The Neuschwanstein Castle", "The Hiroshima Peace Memorial Park", "The Yosemite National Park", "The Yellowstone National Park", "The Canadian Rocky Mountains"]
scenery_descriptions_top30_ziran = ["Grand Canyon", "Yellowstone National Park", "Yosemite National Park", "Zion National Park", "Banff National Park", "Lake Louise", "Rocky Mountain National Park", "Glacier National Park", "Jasper National Park", "Mount Rainier National Park", "Crater Lake National Park", "Great Smoky Mountains National Park", "Denali National Park", "Arches National Park", "Bryce Canyon National Park", "Redwood National and State Parks", "Death Valley National Park", "The Wave", "Niagara Falls", "Plitvice Lakes National Park", "Ha Long Bay", "Mount Everest", "Tianzi Mountain", "Trolltunga", "Geirangerfjord", "Lofoten Islands", "Lake Bled", "Machu Picchu", "Salar de Uyuni", "The Great Barrier Reef"]
scenery_descriptions_top30_man = ["Boardroom meeting", "Power lunch", "Golf course", "Tennis court", "Ski resort", "Private jet", "Luxury yacht", "Exclusive club", "Fine dining restaurant", "Wine tasting event", "Art gallery opening", "Opera house", "Symphony hall", "Charity gala", "Red carpet event", "Fashion show", "Movie premiere", "VIP lounge", "High-end casino", "Private party", "Business conference", "CEO summit", "Investment seminar", "Luxury car dealership", "Private gym", "Polo match", "Sailing regatta", "Horse racing", "Formula One race", "Private island retreat"]

# clothing_descriptions_man = ['collared shirt', 'hoodie', 'T-shirt', 'jacket', 'knit sweater', 'windbreaker', 'down jacket', 'cotton jacket', 'denim jacket', 'shirt', 'leather jacket', 'biker jacket', 'sweater', 'short sleeve shirt', 'work jacket', 'wool sweater', 'long sleeve T-shirt', 'vest', 'polo shirt', 'beast hoodies', 'camo jacket', 'waistcoat', 'summer long sleeve shirt', 'sport jacket', 'workwear', 'running shirt', 'qipao', 'cardigan', 'tight-fitting T-shirt', 'ski suit', 'Washed denim jacket', 'Vest', 'Lightweight blazer', 'Short sleeve shirt', 'Utility jacket', 'Leather jacket', 'Long sleeve polo shirt', 'Sport jacket', 'Denim shirt', 'Stand-collar jacket', 'Short sleeve polo shirt', 'Chiffon shirt', 'Biker jacket', 'Sports vest', 'Leather coat', 'Knit cardigan jacket', 'Long sleeve sweatshirt', 'Long sleeve athletic tee', 'Light jacket', 'Wool vest', 'Faux leather jacket', 'Washed denim coat', 'Baseball jacket', 'Sweatshirt jacket', 'Straw hat', 'Overcoat', 'Field jacket', 'Long coat', 'Short coat', 'Short jacket']
# clothing_descriptions_man = ["衬衣", "毛衣", "衬衣", "美式复古袋鼠兜帽衫", "商务西装", "西装+外套", "不对称设计针织衫", "垂感丝绒衬衫", "立体裁剪短款肯巴风衣外套", "重磅帆布油蜡夹克", "美式街头棒球服", "卡通印花毛呢大衣外套", "休闲百搭上衣", "圆领短袖", "V领短袖", "V领长袖", "针织衫", "夹克", "皮衣", "机车服"]
clothing_descriptions_man = ["Shirt", "Sweater", "Shirt", "American retro kangaroo pocket hooded sweater", "Business suit", "Suit jacket + Coat", "Asymmetric design knit sweater", "Draped velvet shirt", "Short Kenba windbreaker with three-dimensional cutting", "Heavy canvas oil wax jacket", "American street baseball jacket", "Cartoon printed woolen coat", "Casual and versatile top", "Round-neck short-sleeved shirt", "V-neck short-sleeved shirt", "V-neck long-sleeved shirt", "Knit sweater", "Jacket", "Leather jacket", "Motorcycle jacket"]

# clothing_descriptions_man = ["Suit", "Tuxedo", "Blazer", "Dress shirt", "Polo shirt", "Henley shirt", "Button-down shirt", "Dress pants", "Chinos", "Khakis", "Jeans", "Bomber jacket", "Leather jacket", "Denim jacket", "Trench coat", "Peacoat", "Overcoat", "Parka", "Hoodie", "Cardigan", "V-neck sweater", "Crew-neck sweater", "Scarf", "Tie", "Bow tie", "Pocket square", "Cufflinks", "Loafers", "Dress shoes", "Sneakers"]
time_descriptions = [    "10:00 AM",    "2:30 PM",    "7:15 AM",    "11:45 PM",    "6:00 PM",    "9:30 AM",    "3:45 PM",    "8:00 AM",    "1:00 PM",    "5:30 PM",    "12:15 PM",    "4:45 AM",    "11:00 PM",    "8:30 AM",    "2:00 PM",    "6:30 PM",    "10:45 AM",    "12:00 PM",    "7:00 PM",    "9:00 AM"]
posture_verbs = ["Hand in pocket and looking handsome", "Half clench fist and extend hand to block face", "Looking away with a distant gaze", "Holding a prop sign", "In a serious working state", "Looking down at a book", "Posing for a serious photo", "Standing sideways and looking into the distance", "Leaning against a railing", "Sitting on the ground with one foot stretched out"]

# hairstyles = ['Crew Cut', 'Ivy League Cut', 'High and Tight', 'Slicked Back', 'Side Part', 'Undercut', 'French Crop', 'Buzz Cut', 'Textured Crop', 'Pompadour', 'Buzz cut', 'Crew cut', 'Classic slick back', 'Modern slick back', 'Pompadour', 'Side part', 'Quiff', 'Textured crop', 'Comb over', 'French crop', 'Fringe', 'Side swept', 'Spiky hair', 'Messy fringe', 'Short back and sides', 'Curly hair', 'Wavy hair', 'Surfer hair', 'Shaggy hair', 'Mullet', 'Afro', 'Dreadlocks', 'Man bun', 'Top knot', 'Bald', 'High and tight', 'Ivy league', 'Disconnected undercut', 'Undercut', 'Long hair']
# hairstyles = ["飞机头", "短碎发", "潮流蓬松染发", "时尚烫发", "摩根烫", "锡纸烫", "自信背头", "露额二八", "日系卷发", "韩系发型", "型男四六", "商务精英发型", "网红发型" ]
hairstyles = ["Aircraft head", "Short choppy hair", "Trendy fluffy dyed hair", "Fashionable perm", "Morgan perm", "Foil perm", "Confident slicked-back hair", "Two-eight hairline", "Japanese-style curly hair", "Korean-style hairstyle", "Stylish 4-6 haircut", "Business elite hairstyle", "Internet celebrity hairstyle"]


def get_hairstyle() -> str:
    return random.choice(hairstyles)


def get_scenery() -> str:
    return random.choice(scenery_descriptions_new2)


def get_clothing() -> str:
    return random.choice(clothing_descriptions_man)
    # return 'collared shirt'


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
    return "EasyNegative, paintings, (topless:2),sketches, (worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, age spot, glans,extra fingers,fewer fingers,((watermark:2)),((white letters:1))"


def get_prompt() -> str:
    return get_prompt_dict().get('prompt')


def get_prompt_dict() -> dict:
    hairstyle = get_hairstyle()
    scenery = get_scenery()
    clothing = get_clothing()
    _time = get_time()
    posture = get_posture()
    lora = get_lora()
    u_log.print_log(f"当前获取的随机参数：场景：{scenery}， 服装：{clothing}， 时间：{_time}， 姿态：{posture}， 发型：{hairstyle}， lora：{lora}")
    # prompt = f"{lora}(8k, RAW photo, best quality, masterpiece:1.2), (realistic, photo-realistic:1.5), ultra-detailed,background {scenery},{_time}, 1 man, handsome with an Asian facial structure,{posture}, small and well-defined features, delicate and refined appearance, wearing a casual suit with a weight of 1.1, standing on the street with a relaxed and confident demeanor, exuding an air of sophistication and charm, clean-shaven with a focus on his chiseled jawline and defined cheekbones, with his hair styled to perfection, capturing his suave and stylish personality with a touch of raw masculinity."
    prompt = f"{lora}(8k, RAW photo, best quality, masterpiece:1.2), (realistic, photo-realistic:1.5), ultra-detailed, 1 (((man))), (slick-haired scum), handsome with an Asian facial structure, small and well-defined features, delicate and refined appearance, confident demeanor, exuding an air of sophistication and charm, clean-shaven with a focus on his chiseled jawline and defined cheekbones, with his hair styled to perfection, suave and stylish personality with a touch of raw masculinity.beautiful detailed sky,{scenery},{_time},{posture},dating, (smile:1.1),(closed mouth) ,({clothing}:1.1),({hairstyle}:1.2)."
    return {
        'scenery': scenery,
        'clothing': clothing,
        'time': _time,
        'posture': posture,
        'prompt': prompt,
    }


def get_batch_size() -> int:
    """获取每次生成多少张图，默认1，显卡的显存够的话可以调整多些"""
    lst = [1, 2, 4]
    return random.choice(lst)
    # return 1


def get_steps() -> int:
    # lst = [30, 50, 60, 80, 90, 130]
    # return random.choice(lst)
    return 150


def get_cfg_scale() -> float:
    return round(random.uniform(7.0, 7.6), 1)


def get_sampler_name() -> str:
    return 'DPM++ 2M Karras'


def get_sd_model_checkpoint() -> str:
    return "chilloutmix_NiPrunedFp32Fix"


def get_width_height() -> (int, int):
    return 768, 1024


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
