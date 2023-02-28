#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 19:29
# @Author  : Samge
import os
import time

import requests
from PIL import PngImagePlugin

from test.utils import u_config, u_log, u_prompt_man, u_prompt, u_file

false = False
true = True
null = None


def get_save_dir() -> str:
    """获取图片的输出目录"""
    # 获取当前文件的绝对路径
    current_path = os.path.abspath(__file__)
    return u_file.join(u_file.get_parent_path(current_path, 3), '/outputs/txt2img-images/api-test')


def get_img_info(i, host: str = None):
    """ 获取图片配置信息 """
    try:
        png_payload = {
            "image": "data:image/png;base64," + i
        }
        response2 = requests.post(url=u_config.get_api_imginfo(host), json=png_payload)
        imginfo = PngImagePlugin.PngInfo()
        imginfo.add_text("parameters", response2.json().get("info"))
        return imginfo
    except Exception as e:
        u_log.print_log(f'获取图片配置信息 失败：{e}')
        return None


def test_txt2img(count: int, is_man: bool = False, host: str = None):
    """
    文字转图片
    Args:
        count: 当前执行次数
        is_man: 是否男
        host: 自定义服务器地址
    Returns:
    """
    tag = 'man' if is_man else 'women'
    _config = u_prompt_man.get_config() if is_man else u_prompt.get_config()
    u_log.print_log(f"\n【{count}-{tag}-{host or u_config.api_base_url}】正在执行（steps={_config.get('steps')}，batch_size={_config.get('batch_size')}），请稍后……")
    payload = generate_payload_t2i(_config)
    try:
        response = requests.post(url=u_config.get_api_txt2img(host), json=payload)
        if response.status_code != 200:
            u_log.print_log(f"执行失败：status_code = {response.status_code}")
            time.sleep(5)
            return
        r = eval(response.text)
        for image_base64 in r.get('images') or []:
            u_file.save_img(image_base64, _config, get_save_dir(), is_man=is_man, host=host)
            time.sleep(1)  # 避免重名
        u_log.print_log('执行完成')
    except Exception as e:
        u_log.print_log(f"执行失败：{e}")
        time.sleep(5)


def generate_payload_t2i(_config: dict) -> dict:
    """生成 文生图 的请求体"""
    return {
      "enable_hr": false,
      "denoising_strength": 0,
      "firstphase_width": 0,
      "firstphase_height": 0,
      "hr_scale": 2,
      "hr_upscaler": "",
      "hr_second_pass_steps": 0,
      "hr_resize_x": 0,
      "hr_resize_y": 0,
      "prompt": _config.get('prompt'),
      "styles": [
        ""
      ],
      "seed": _config.get('seed') or -1,
      "subseed": -1,
      "subseed_strength": 0,
      "seed_resize_from_h": -1,
      "seed_resize_from_w": -1,
      "sampler_name": _config.get('sampler_name'),
      "batch_size": _config.get('batch_size'),
      "n_iter": 1,
      "steps": _config.get('steps'),
      "cfg_scale": _config.get('cfg_scale'),
      "width": _config.get('width'),
      "height": _config.get('height'),
      "restore_faces": false,
      "tiling": false,
      "negative_prompt": _config.get('negative_prompt'),
      "eta": 0,
      "s_churn": 0,
      "s_tmax": 0,
      "s_tmin": 0,
      "s_noise": 1,
      "override_settings": {},
      "override_settings_restore_afterwards": true,
      "script_args": [],
      "sampler_index": _config.get('sampler_index'),
      "sd_model_checkpoint": _config.get('sd_model_checkpoint')
    }