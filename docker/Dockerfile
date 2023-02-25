FROM samge/base-stable-diffusion-webui:latest
LABEL org.opencontainers.image.authors="samgeapp@gmail.com"

RUN export all_proxy=socks5://192.168.3.169:7890 && \
    pip install open_clip_torch && \
    pip install gdown && \
    pip install safetensors


VOLUME stable-diffusion-webui/models
VOLUME stable-diffusion-webui/repositories
VOLUME stable-diffusion-webui/outputs
EXPOSE 7860
EXPOSE 7861

# 默认运行webui，如果需要以api方式运行，加上命令行参数：--nowebui
CMD ["python", "webui.py", "--listen"]