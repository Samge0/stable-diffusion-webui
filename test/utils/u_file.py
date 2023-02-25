#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2023/2/23 19:22
# @Author  : Samge
import os.path
import time

from modules import extra_networks
from test.utils import u_prompt, u_date, u_log, u_common, u_http, u_str
import io
import base64
from PIL import Image


def join(root_dir: str, path: str) -> str:
    """
    统一将两个路径用 / 拼接
    """
    if not root_dir:
        raise ValueError('root_dir cannot be empty!')
    root_dir = root_dir.replace('\\', '/')
    path = (path or '').replace('\\', '/')
    if root_dir.endswith('/'):
        root_dir = root_dir[:len(root_dir)-1]
    if path.startswith('/'):
        path = path[1:]
    return f'{root_dir}/{path}'


def get_parent_path(curr_file_path, step=1) -> str:
    """获取父级目录"""
    _split = (curr_file_path or '').split(os.path.sep)
    if step > len(_split):
        raise ValueError("step over maximum directory level!")
    return os.path.sep.join(_split[:-step])


def save(_txt: str, _path: str, _type: str = 'w+') -> bool:
    """保存文件"""
    try:
        with open(_path, _type, encoding='utf-8') as f:
            f.write(_txt)
            f.flush()
            f.close()
        return True
    except:
        return False


def read(_path: str) -> str:
    """读取文件"""
    if os.path.exists(_path) is False:
        return ''
    with open(_path, "r", encoding='utf-8') as f:
        txt = f.read()
        f.close()
        return txt or ''


def size(file_path) -> float:
    """读取文件大小，单位：M"""
    if not file_path or os.path.exists(file_path) is False:
        return 0
    return os.path.getsize(file_path) / 1024 / 1024


def file_name_max_len() -> int:
    """获取文件名最大长度限制"""
    max_len = 0
    try:
        for i in range(1, 10**10):
            name = "m" * i
            with open(name, 'w') as ofs:
                ofs.write("1")
                ofs.close()
            os.remove(name)
            max_len = i
    except IOError as ioe:
        print("Maximum length of file name is: {}".format(max_len))
    return max_len


def dir_name_max_len() -> int:
    """ 获取目录最大限制长度 """
    max_len = 0
    try:
        for i in range(1, 10**10):
            name = "m" * i
            os.mkdir(name)
            os.rmdir(name)
            max_len = i
    except OSError as ioe:
        print("Maximum length of directory name is: {}".format(max_len))
    return max_len


class MaxFileLenModel(object):
    max_file_len = 0
    max_dir_len = 0

    def __init__(self):
        self.max_file_len = file_name_max_len()
        self.max_dir_len = dir_name_max_len()


maxFileLenModel = MaxFileLenModel()


def _format_str(v: str) -> str:
    """ 空格句子首字母大写 + 移除空格等字符 """
    return u_str.keep_chinese_alphanumeric(u_str.initial_capital(v))


def get_ext_model_info(_config: dict) -> str:
    """获取扩展模型信息"""
    if not _config:
        return ''
    prompt = _config.get('prompt')
    prompts = [prompt]
    _, extra_network_data = extra_networks.parse_prompts(prompts)
    if not extra_network_data:
        return ''
    tmp_lst = []
    for ext_type, params in extra_network_data.items():
        tmp_lst.append(ext_type)
        for param in params:
            model_name = param.items[0].lower().replace('dolllikeness', '')
            model_percentage = int(u_common.str2float(param.items[1]) * 10)
            tmp_lst.append(model_name)
            tmp_lst.append(model_percentage)
    return '_'.join(str(v) for v in tmp_lst)


def get_file_name(_config: dict) -> str:
    """ 获取文件名
    格式：时间戳_种子_步数_批次数_cfg_ext模型_场景_服装_姿势
    """
    file_max_len = maxFileLenModel.max_file_len
    prompt_dict = _config.get('prompt_dict') or {}
    scenery = _format_str(prompt_dict.get('scenery'))  # 场景
    clothing = _format_str(prompt_dict.get('clothing'))  # 服饰
    _time = _format_str(prompt_dict.get('time'))  # 时间
    posture = _format_str(prompt_dict.get('posture'))  # 姿态
    seed = f"seed{str(_config.get('seed')).replace('-1', '1')}"  # 种子
    steps = f"steps{_config.get('steps')}"  # 步数
    cfg_scale = f"cfg{int(_config.get('cfg_scale') * 10)}"  # 服从比例
    batch_size = f"batch{_config.get('batch_size')}"  # 批次数
    ext_model_info = get_ext_model_info(_config)  # 扩展模型信息
    tmp_lst = [
        u_date.get_timestamp(),
        seed,
        steps,
        batch_size,
        cfg_scale,
        ext_model_info,
        scenery,
        clothing,
        _time,
        posture
    ]
    file_name = '_'.join(str(v) for v in tmp_lst)
    file_name = file_name[:file_max_len]
    return f'{file_name}.png'


def get_save_path(_config: dict, root_dir: str, is_man=False) -> (str, str):
    """ 获取文件保存路径 """
    # 拼接目录路径
    path_tag = 'man' if is_man else 'women'
    prompt_dict = _config.get('prompt_dict') or {}
    scenery = _format_str(prompt_dict.get('scenery') or 'default_scenery')
    curr_date = u_date.get_today_str(f='%Y-%m-%d')
    save_dir = join(root_dir, f'/{curr_date}/{path_tag}/{scenery}')
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    # 拼接文件路径
    file_name = get_file_name(_config)

    # 细分类的保存路径 & 所有文件保存路径（存一个汇总的方便后期处理）
    category_save_path = f"{save_dir}/{file_name}"
    all_dir = join(root_dir, f'/{curr_date}/{path_tag}/all')
    if not os.path.exists(all_dir):
        os.makedirs(all_dir)
    all_save_path = f"{all_dir}/{file_name}"
    return category_save_path, all_save_path


def save_img(image_base64, _config, root_dir, is_man=False):
    """ 保存图片 """
    try:
        u_log.print_log(f"正在保存……")
        category_save_path, all_save_path = get_save_path(_config, root_dir, is_man)
        save_img_by_path(category_save_path, image_base64)
        save_img_by_path(all_save_path, image_base64)
    except Exception as e:
        u_log.print_log(f'保存 失败：{e}')


def save_img_by_path(save_path, image_base64, max_try_times=10):
    try:
        image = Image.open(io.BytesIO(base64.b64decode(image_base64.split(",", 1)[0])))
        image.save(save_path, pnginfo=u_http.get_img_info(image_base64))
        u_log.print_log(f"保存在：{save_path}")
    except Exception as e:
        if max_try_times <= 0:
            u_log.print_log(f'保存 失败：{e}')
            return
        # 保存失败基本是由于文件路径过长，尝试从右往左截断部分_后面的内容
        save_path_new = save_path.split('.png')[0]
        last_underscore_index = save_path_new.rfind('_')
        save_path_new = save_path_new[: last_underscore_index]
        save_path_new = f'{save_path_new}.png'
        u_log.print_log(f'尝试截断文件名再进行保存，截断后的图片路径：{save_path_new}')
        max_try_times -= 1
        save_img_by_path(save_path_new, image_base64, max_try_times=max_try_times)


if __name__ == '__main__':
    _config = u_prompt.get_config()
    for k, v in _config.items():
        print(f'{k}: {v}')
    # print(get_save_path(_config))
    print(get_save_path(_config))
