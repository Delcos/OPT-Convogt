# OPT-convogpt
## Now with 3D Tensor Support!

This is an updated version of convogpt that I've modified to run OPT models. It can also run any other LLM pytorch model with just 2 lines of code being changed to whatever model you're using.

Aside from this, it is now able to get repeated inputs instead of running once and outputting a value.

## ⚙️ Models
| Model ID   | Parameter Count | Training Method |
|------------|-----------------|-----------------|
| [350m](https://huggingface.co/facebook/opt-350m)
| [2.7b](https://huggingface.co/facebook/opt-2.7b)
| [6.7b](https://huggingface.co/facebook/opt-6.7b)
| [66b](https://huggingface.co/facebook/opt-66b) | This is a massive model, it will NOT run on any consumer hardware. Don't download this unless you know what you're doing.

## 🔑 Setup

```shell
git clone git@github.com:harubaru/convogpt.git
cd convogpt
pip install protobuf==3.20.*
python -m pip install -r requirements
```
