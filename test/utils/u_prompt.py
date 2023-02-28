#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 19:22
# @Author  : Samge
import random

from test.utils import u_log, u_prompt_man, u_prompt

# <lora:koreanDollLikeness_v10:0.3>,
# <lora:taiwanDollLikeness_v10:0.2>
# <lora:japaneseDollLikeness_v10:0.2>
# <lora:asiangirllikeness_v10:0.1>
# <lora:artErosAerosATribute_aerosNovae:0.1>
# <lora:evoart_v20:0.1>
# <lora:pureerosface_v1:0.1>"

# scenery_descriptions_new2 = ["星巴克咖啡店", "香港街头", "香港太平山上", "深圳海边", "深圳平安大厦", "深圳梧桐山", "音乐厅", "电影院", "麦当劳店里", "肯德基店里", "古风小巷", "福建鼓浪屿", "飞龙雪山", "西藏", "青海湖", "夏威夷海边", "城中村"]
scenery_descriptions_new2 = ["Starbucks coffee shop", "Hong Kong street", "Victoria Peak in Hong Kong", "Beach in Shenzhen", "Ping An Finance Center in Shenzhen", "Wutong Mountain in Shenzhen", "Concert hall", "Movie theater", "Inside McDonald's", "Inside KFC", "Ancient-style alley", "Gulangyu Island in Fujian", "Jade Dragon Snow Mountain", "Tibet", "Qinghai Lake", "Beach in Hawaii", "Urban village"]

scenery_descriptions_new = ["Botanical Garden", "Rooftop bar", "Hot air balloon ride", "Beach picnic", "Art museum", "Winery tour", "Romantic restaurant", "Horse-drawn carriage ride", "Sunset cruise", "Candlelit concert", "Ice skating rink", "Fancy cocktail bar", "Opera house", "Boutique hotel", "Nature hike", "Champagne brunch", "Cooking class", "Drive-in movie theater", "Aquarium", "Dinner theater", "Scenic train ride", "Salsa dancing class", "Vintage flea market", "Roller skating rink", "Mansion tour", "Amusement park", "Poetry reading", "Sushi-making class", "Street festival", "Ballet performance", "detailed cafe"]
scenery_descriptions_top30_world = ["The Great Wall of China", "Machu Picchu", "Taj Mahal", "Petra", "Angkor Wat", "The Colosseum", "The Grand Canyon", "Niagara Falls", "Santorini", "The Pyramids of Giza", "The Acropolis of Athens", "The Eiffel Tower", "The Statue of Liberty", "The Grand Palace", "Stonehenge", "The Vatican City", "The Parthenon", "The Christ the Redeemer Statue", "The Alhambra", "The Sagrada Familia", "The Great Barrier Reef", "The Sydney Opera House", "The Tower Bridge", "The Big Ben", "The Palace of Versailles", "The Neuschwanstein Castle", "The Hiroshima Peace Memorial Park", "The Yosemite National Park", "The Yellowstone National Park", "The Canadian Rocky Mountains"]
scenery_descriptions_top30_ziran = ["Grand Canyon", "Yellowstone National Park", "Yosemite National Park", "Zion National Park", "Banff National Park", "Lake Louise", "Rocky Mountain National Park", "Glacier National Park", "Jasper National Park", "Mount Rainier National Park", "Crater Lake National Park", "Great Smoky Mountains National Park", "Denali National Park", "Arches National Park", "Bryce Canyon National Park", "Redwood National and State Parks", "Death Valley National Park", "The Wave", "Niagara Falls", "Plitvice Lakes National Park", "Ha Long Bay", "Mount Everest", "Tianzi Mountain", "Trolltunga", "Geirangerfjord", "Lofoten Islands", "Lake Bled", "Machu Picchu", "Salar de Uyuni", "The Great Barrier Reef"]

scenery_descriptions_top30_man = ["Boardroom meeting", "Power lunch", "Golf course", "Tennis court", "Ski resort", "Private jet", "Luxury yacht", "Exclusive club", "Fine dining restaurant", "Wine tasting event", "Art gallery opening", "Opera house", "Symphony hall", "Charity gala", "Red carpet event", "Fashion show", "Movie premiere", "VIP lounge", "High-end casino", "Private party", "Business conference", "CEO summit", "Investment seminar", "Luxury car dealership", "Private gym", "Polo match", "Sailing regatta", "Horse racing", "Formula One race", "Private island retreat"]

clothing_descriptions_new = ["All-match top", "Anime Joint Top", "Artistic Top", "Hong Kong-style Japanese-style all-match top", "Premium Skinny Double Zip Top", "French High Neck Embroidered Top", "High fashion comfortable top", "Premium Slim Design Top", "Superior Loose Lazy Top", "Superior French Lapel Top", "Superior Striped Sloffy Top", "Skinny Gentle Lazy Top", "advanced Slim temperament top", "Loose sweet cute top", "high-end retro Couples top", "Loose hooded sweater, comfortable", "Sweater", "Wrap blouse", "Mock-neck blouse", "Collared blouse", "Loose Knit", "Loose slimming college style", "Coat, Suit Collar"]
clothing_descriptions_new2 = ["collared shirt", "Button-up shirt", "Tuxedo shirt", "Polo shirt", "Blouse", "Denim shirt", "Oxford shirt", "Wrap shirt", "Chambray shirt", "Tie-neck blouse", "T-shirt",  "Blouse", "Button-up shirt",   "Peplum top", "Tube top", "Bustier",   "Polo shirt", "Sweatshirt",  "Cardigan", "Blazer", "Denim jacket", "Leather jacket", "Bomber jacket", "Poncho", "Kimono", "Tunic", "Camisole", "Cropped sweater", "Sleeveless turtleneck", "Bell sleeve top"]
clothing_descriptions_56minzu = ["Hanfu", "Daicloth", "Qipao", "Hui clothing", "Miao clothing", "Uyghur clothing", "Yi clothing", "Tibetan clothing", "Deel", "Buyi clothing", "Hanbok", "Dong clothing", "Yao clothing", "Bai clothing", "Hani clothing", "Kazakh clothing", "Li clothing", "Dai clothing", "She clothing", "Tujia clothing", "Naxi clothing", "Qiang clothing", "Tu clothing", "Xibe clothing", "Jingpo clothing", "Salar clothing", "Blang clothing", "Maonan clothing", "Tajik clothing", "Pumi clothing", "Uzbek clothing", "Russian clothing", "Achang clothing", "Oroqen clothing", "Daur clothing", "Mulao clothing", "Gin clothing", "Ewenki clothing", "Lhoba clothing", "Jino clothing", "De'ang clothing", "Kyrgyz clothing", "Bao'an clothing", "Russian clothing", "Uzbek clothing", "Evenki clothing", "Dongxiang clothing", "Gelao clothing", "Tatar clothing", "Hezhen clothing", "Gaoshan clothing", "Lahu clothing", "Gelo clothing", "Monba clothing", "Luoba clothing", "Jiarong clothing"]

clothing_descriptions_man = ["Suit", "Tuxedo", "Blazer", "Dress shirt", "Polo shirt", "Henley shirt", "Button-down shirt", "Dress pants", "Chinos", "Khakis", "Jeans", "Bomber jacket", "Leather jacket", "Denim jacket", "Trench coat", "Peacoat", "Overcoat", "Parka", "Hoodie", "Cardigan", "V-neck sweater", "Crew-neck sweater", "Scarf", "Tie", "Bow tie", "Pocket square", "Cufflinks", "Loafers", "Dress shoes", "Sneakers"]

scenery_descriptions = [    "The sun setting over the ocean, casting a golden glow across the waves",    "A snow-capped mountain peak towering over a crystal-clear lake",    "A misty forest with sunlight streaming through the trees",    "A field of wildflowers in full bloom, with bees buzzing among them",    "A rainbow arching across a waterfall",    "A desert landscape with sand dunes stretching as far as the eye can see",    "A rocky coastline with waves crashing against the cliffs",    "A meadow with a herd of grazing horses",    "A city skyline at night, with skyscrapers lit up like beacons",    "A tropical beach with palm trees swaying in the breeze",    "A lush green valley surrounded by towering mountains",    "A peaceful countryside with a quaint farmhouse and grazing sheep",    "An ancient ruin with intricate stonework and breathtaking views",    "A vibrant garden bursting with colorful blooms",    "A tranquil lake surrounded by forests and hills",    "A picturesque village nestled in a verdant valley",    "A vast, open plain with wild horses running free",    "A grand waterfall plunging into a deep, misty canyon",    "A snow-covered forest with icicles glistening in the sunlight",    "A dramatic cliffside with sweeping views of the ocean"]
scenery_descriptions2 = [    "Golden sunset over the ocean",    "Snowy mountain peak reflected in a clear lake",    "Misty forest with sunlight shining through the trees",    "Field of colorful wildflowers with buzzing bees",    "Rainbow over a waterfall",    "Endless sand dunes in a desert",    "Rocky coastline with waves crashing",    "Herd of horses grazing in a meadow",    "City skyline lit up at night",    "Palm trees swaying on a tropical beach",    "Green valley surrounded by tall mountains",    "Quaint countryside with grazing sheep",    "Ancient ruins with stunning views",    "Vibrant garden full of colorful blooms",    "Tranquil lake surrounded by hills",    "Picturesque village in a verdant valley",    "Wild horses running free on a vast plain",    "Grand waterfall plunging into a misty canyon",    "Snow-covered forest with glistening icicles",    "Dramatic cliffside with sweeping ocean views"]
clothing_descriptions = [    "A flowy sundress with a vibrant floral pattern and delicate spaghetti straps",    "A sleek and sophisticated jumpsuit in a rich emerald green",    "A bohemian-inspired maxi skirt paired with a cropped denim jacket",    "A classic little black dress with a fitted silhouette and lace detailing",    "A cozy oversized sweater with a chunky knit texture and cable knit sleeves",    "A playful romper in a bold geometric print with a ruffled neckline",    "A chic and timeless trench coat in a soft beige hue",    "A flirty off-the-shoulder top with billowing sleeves and a cropped hemline",    "A tailored blazer in a striking plaid pattern, paired with matching trousers",    "A breezy wrap dress in a lightweight fabric, perfect for a summer day",    "A sleek and modern leather jacket with silver hardware",    "A whimsical midi dress with a tiered skirt and intricate embroidery",    "A bohemian-inspired crochet top with bell sleeves and tassel detailing",    "A feminine and flirty skirt in a playful polka dot print",    "A cozy knit cardigan with oversized buttons and a slouchy fit",    "A bold and statement-making jumpsuit in a bright fuchsia hue",    "A classic white blouse with a romantic ruffle neckline",    "A sleek and sexy bodycon dress in a rich burgundy shade",    "A flowy and romantic maxi dress in a delicate floral print",    "A playful mini skirt in a vibrant shade of coral"]
clothing_descriptions2 = [    "A flowy pastel-colored qipao dress with delicate floral embroidery",    "A cute crop top with a high-waisted skirt in a traditional Korean print",    "A playful romper with a cherry blossom pattern and flutter sleeves",    "A cozy sweater vest over a collared shirt, paired with a plaid skirt and knee-high socks",    "A classic cheongsam dress in a bold red color with gold button accents",    "A cute sailor collar dress in a fun polka dot print with a flared skirt",    "A traditional Japanese yukata with a vibrant floral design and obi sash",    "A chic and modern hanbok-inspired dress in a muted color palette",    "A playful lolita-style dress with a whimsical print and lace trim",    "A cute sailor outfit with a striped top, navy shorts, and a sailor hat",    "A traditional Chinese tangzhuang jacket over a high-waisted skirt and blouse",    "A cozy knit cardigan over a plaid mini skirt and knee-high boots",    "A cute and playful panda-themed dress with a peter pan collar",    "A traditional Vietnamese ao dai dress in a bright and bold hue",    "A chic and modern take on a Chinese cheongsam with a sleek silhouette and embroidered accents",    "A cute schoolgirl-inspired outfit with a plaid skirt and knee-high socks",    "A sweet and feminine qipao dress in a soft pink color with delicate lace detailing",    "A traditional Korean hanbok in a pastel-colored floral print",    "A playful and whimsical fairy-inspired outfit with a tulle skirt and floral crown",    "A cute and comfy oversized hoodie with a cute cartoon character print"]

time_descriptions = [    "10:00 AM",    "2:30 PM",    "7:15 AM",    "11:45 PM",    "6:00 PM",    "9:30 AM",    "3:45 PM",    "8:00 AM",    "1:00 PM",    "5:30 PM",    "12:15 PM",    "4:45 AM",    "11:00 PM",    "8:30 AM",    "2:00 PM",    "6:30 PM",    "10:45 AM",    "12:00 PM",    "7:00 PM",    "9:00 AM"]
photo_poses = ["Sitting", "Slightly tilted head with a slight smile", "Holding an umbrella", "Leaning on a railing", "Standing sideways or looking back", "Touching or tilting head back", "Standing in a corner", "Sitting by a doorway", "Sitting under a tree"]


hairstyles = ["long hair,floating hair", "Fashionable big wavy curls", "Long ponytail", "Fluffy short hair", "Light mature curls", "Korean style side-parted medium-length hair with temperament", "Internet-famous big wavy hair with side parting", "Bob hairstyle ending at the chin"]


# prompt = "<lora:koreanDollLikeness_v10:0.3>,<lora:taiwanDollLikeness_v10:0.2>,<lora:japaneseDollLikeness_v10:0.2>(8k, RAW photo, best quality, masterpiece:1.2), (realistic, photo-realistic:1.37), ultra-detailed, 1 girl,cute, solo,{scenery},{time},{posture},dating,(nose blush),(smile:1.1),(closed mouth) medium breasts,beautiful detailed eyes,({clothing}:1.1), bowtie,pleated skirt,(short hair:1.2),floating hair"
# prompt = "<lora:koreanDollLikeness_v10:0.3>,<lora:taiwanDollLikeness_v10:0.2>(8k, RAW photo, best quality, masterpiece:1.2), (realistic, photo-realistic:1.37), ultra-detailed, 1 girl,cute, solo,beautiful detailed sky,on seaside beach,night,sitting,dating,(nose blush),(smile:1.1),(closed mouth) medium breasts,beautiful detailed eyes,(collared shirt:1.1), bowtie,pleated skirt,(short hair:1.2),floating hair <lora:japaneseDollLikeness_v10:0.2> <lora:asiangirllikeness_v10:0.1> <lora:artErosAerosATribute_aerosNovae:0.1> <lora:evoart_v20:0.1> <lora:pureerosface_v1:0.1>"
# prompt = "<lora:koreanDollLikeness_v10:0.3>,<lora:taiwanDollLikeness_v10:0.2>(8k, RAW photo, best quality, masterpiece:1.2), (realistic, photo-realistic:1.37), ultra-detailed, 1 girl,cute, solo,beautiful detailed sky,Traffic light intersection,night,sitting,dating,(nose blush),(smile:1.1),(closed mouth) medium breasts,beautiful detailed eyes,(collared shirt:1.1), bowtie,pleated skirt,(short hair:1.2),floating hair"


def get_hairstyle() -> str:
    return random.choice(hairstyles)


def get_scenery() -> str:
    return random.choice(scenery_descriptions_new2)


def get_clothing() -> str:
    return random.choice(clothing_descriptions_new)
    # return random.choice(clothing_descriptions_new2 + clothing_descriptions_56minzu)
    # return 'collared shirt'

def get_time() -> str:
    # return random.choice(time_descriptions)
    return 'night'


def get_posture() -> str:
    return random.choice(photo_poses)
    # return 'sitting'


def get_lora() -> str:
    default_lora = "<lora:koreanDollLikeness_v10:0.3>,<lora:taiwanDollLikeness_v10:0.2>"
    num = random.choice([0.0, 0.1, 0.2])
    if num == 0:
        return default_lora
    return f"{default_lora},<lora:japaneseDollLikeness_v10:{num}>"


def get_negative_prompt() -> str:
    return "EasyNegative, paintings, sketches, (bare chest:2), (worst quality:2), (low quality:2), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, age spot, glans,extra fingers,fewer fingers,((watermark:2)),((white letters:1))"


def get_prompt() -> str:
    return get_prompt_dict().get('prompt')


def get_prompt_dict(is_man: bool = False) -> dict:
    hairstyle = get_hairstyle()
    scenery = get_scenery()
    clothing = get_clothing()
    _time = get_time()
    posture = get_posture()
    lora = get_lora()
    u_log.print_log(f"当前获取的随机参数：场景：{scenery}， 服装：{clothing}， 时间：{_time}， 姿态：{posture}， 发型：{hairstyle}， lora：{lora}")
    prompt = f"{lora}(8k, RAW photo, best quality, masterpiece:1.2), (realistic, photo-realistic:1.37), ultra-detailed, 1 girl,cute, solo,beautiful detailed sky,background {scenery},{_time},{posture},dating,(nose blush),(smile:1.1),(closed mouth) medium small chest,beautiful detailed eyes,({clothing}:1.1), pleated long skirt,({hairstyle}:1.2)"
    # prompt = f"{lora}(8k, RAW photo, best quality, masterpiece:1.2), (realistic, photo-realistic:1.37), ultra-detailed, 1 girl,cute, solo,beautiful detailed sky,background {scenery},{_time},{posture},dating,(nose blush),(smile:1.1),(closed mouth) medium breasts,beautiful detailed eyes,({clothing}:1.1), bowtie,pleated skirt,(short hair:1.2),floating hair"
    print(prompt)
    return {
        'scenery': scenery,
        'clothing': clothing,
        'time': _time,
        'posture': posture,
        'prompt': prompt,
    }


def get_batch_size() -> int:
    """获取每次生成多少张图，默认1，显卡的显存够的话可以调整多些"""
    # lst = [1, 2, 4, 8]
    # return random.choice(lst)
    return 1


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
