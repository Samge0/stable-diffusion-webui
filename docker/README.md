## Stable Diffusion webui的docker镜像构建
这里拆分pytorch基础包、Stable Diffusion webui基础包只是为了加快后续的构建速度，因为两个基础包所需要的依赖size都比较大、耗时。

### 构建pytorch基准包
```shell
docker build . -t samge/base-pytorch131 -f docker/DockerfilePytorchLatest
```

### 构建Stable Diffusion webui基准包
```shell
docker build . -t samge/base-stable-diffusion-webui -f docker/DockerfileSdBase
```

### 构建Stable Diffusion webui正式包
```shell
docker build . -t samge/stable-diffusion-webui -f docker/Dockerfile
```

### 运行docker镜像（至于 nvidia-docker 命令这里就不展开说明了）
这里的`/home/samge/docker_data/stable-diffusion-webui`需要替换为使用者的本地映射路径。
```shell
nvidia-docker run -d \
--name sdui \
-p 17860:7860 \
-v /home/samge/docker_data/stable-diffusion-webui/models:/stable-diffusion-webui/models \
-v /home/samge/docker_data/stable-diffusion-webui/repositories:/stable-diffusion-webui/repositories \
-v /home/samge/docker_data/stable-diffusion-webui/outputs:/stable-diffusion-webui/outputs \
--pull=always \
--restart always \
--runtime=nvidia \
--ipc=host \
samge/stable-diffusion-webui:latest
```

### models跟repositories的下载：
--来自百度网盘超级会员V4的分享
这两个文件夹放在百度网盘上了，需要的自行下载：[StableDiffusionWebui-models-repositories](https://pan.baidu.com/s/1wPKvOwvruR9yQvrwEqMGCA?pwd=4vk9 )，然后配置到对应的docker映射目录上即可。
```text
models：存放模型的文件夹；
repositories：其他所需要依赖的仓库；
```

网盘上放置的是常用模型，如果需要其他模型可自己到[https://civitai.com/](https://civitai.com/)自行下载即可。
```text
主要模型：models/Stable-diffusion/chilloutmix_NiPrunedFp32Fix.safetensors (3.97G)
日本脸：models/Lora/japaneseDollLikeness_v10.safetensors (144M)
韩国脸：models/Lora/koreanDollLikeness_v10.safetensors (144M)
台湾脸：models/Lora/taiwanDollLikeness_v10.safetensors (144M)
男脸：models/Lora/patrickBatemanChristian_patrickBatemanV1.safetensors (144M)
```

### 其他说明 
如果需要跨机器复制models文件夹，可以用scp复制过去，其中`xxx`是使用者个人用户名：
```shell
mkdir - p /home/xxx/docker_data/stable-diffusion-webui
scp -rp models xxx@192.168.x.xx:/home/xxx/docker_data/stable-diffusion-webui
scp -rp repositories xxx@192.168.x.xx:/home/xxx/docker_data/stable-diffusion-webui
```