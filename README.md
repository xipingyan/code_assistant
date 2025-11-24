# Code Assistant

A customizable code assistant powered by the latest open-source Large Language Models (LLMs) running on your local iGPU. This project enables you to leverage powerful coding AI capabilities without relying on cloud services, ensuring privacy and reducing latency.

## Overview

Code Assistant allows you to create your own intelligent coding companion using state-of-the-art open-source models like **Qwen2.5-Coder-7B-Instruct**. By utilizing your local integrated GPU (iGPU), you can enjoy:

- **Privacy**: Your code and queries never leave your machine
- **Cost-effective**: No subscription fees or API costs
- **Low latency**: Fast responses without network overhead
- **Customization**: Tailor the assistant to your specific needs and workflow

## Features

- 🚀 **Local LLM Execution**: Run powerful code generation models on your local hardware
- 🎯 **iGPU Optimization**: Optimized for integrated GPUs to maximize performance
- 🔧 **Easy Configuration**: Simple setup process to get started quickly
- 📝 **Code Completion**: Intelligent code suggestions and auto-completion
- 💡 **Code Explanation**: Get explanations for complex code snippets
- 🐛 **Debugging Assistance**: Help with identifying and fixing issues
- 🔄 **Multiple Model Support**: Compatible with various open-source LLM models

## Supported Models

The assistant supports various open-source code-focused LLMs, including:

- **Qwen2.5-Coder-7B-Instruct** (Recommended)
- **CodeLlama**
- **StarCoder**
- **WizardCoder**
- And other compatible models

## Requirements

### Hardware Requirements

- **CPU**: Modern x86_64 or ARM64 processor
- **RAM**: Minimum 8GB (16GB recommended)
- **iGPU**: Integrated GPU with compute capability (Intel Iris Xe, AMD Radeon Graphics, etc.)
- **Storage**: At least 10GB free space for model files

### Software Requirements

- **Operating System**: Linux, macOS, or Windows
- **Python**: 3.8 or higher
- **GPU Drivers**: Latest drivers for your iGPU

## Installation

> **Note**: This project is in early development. The following installation steps describe the planned setup process. Some files and features may not yet be available.

### 1. Clone the Repository

```bash
git clone https://github.com/xipingyan/code_assistant.git
cd code_assistant
```

### 2. Install Dependencies

```bash
# Dependencies will be specified in requirements.txt
pip install -r requirements.txt
```

### 3. Download the Model

Download your preferred model (e.g., Qwen2.5-Coder-7B-Instruct):

You can download models from [Hugging Face](https://huggingface.co/):

```bash
# Using Hugging Face CLI
huggingface-cli download Qwen/Qwen2.5-Coder-7B-Instruct --local-dir ./models/qwen2.5-coder-7b

# Or use git-lfs
git lfs install
git clone https://huggingface.co/Qwen/Qwen2.5-Coder-7B-Instruct ./models/qwen2.5-coder-7b
```

### 4. Configure the Assistant

Configuration options will be provided through command-line arguments or a configuration file. Example configuration format:

```bash
# Configuration file (config.yaml) format example
# Create this file based on your preferences
```

## Usage

> **Note**: The project is currently in development. Usage instructions will be updated as features are implemented.

### Basic Usage

Start the code assistant:

```bash
# Command will be available once implemented
python code_assistant.py
```

### Interactive Mode

Launch the interactive console:

```bash
python code_assistant.py --interactive
```

### API Mode

Run as a local API server:

```bash
python code_assistant.py --server --port 8080
```

### Integration with IDEs

The code assistant is planned to integrate with popular IDEs:

- **VS Code**: Extension support planned
- **PyCharm**: Plugin support planned
- **Neovim/Vim**: LSP integration planned

## Configuration

Example configuration format (config.yaml):

```yaml
# This is a planned configuration format
model:
  name: "Qwen2.5-Coder-7B-Instruct"
  path: "./models/qwen2.5-coder-7b"
  
gpu:
  device: "igpu"
  max_memory: "8GB"
  
generation:
  max_tokens: 1024
  temperature: 0.7
  top_p: 0.95
```

## Examples

### Code Completion

```python
# Type your code and get intelligent suggestions
def calculate_fibonacci(n):
    # The assistant will suggest the implementation
```

### Code Explanation

```bash
# Ask the assistant to explain code
> explain: def memoize(func): ...
```

### Debugging

```bash
# Get help with debugging
> debug: Why is my function returning None?
```

## Performance Tips

1. **Optimize Memory**: Adjust `max_memory` in config to match your system
2. **Temperature Settings**: Lower temperature (0.5-0.7) for more deterministic code
3. **Batch Processing**: Process multiple requests together for efficiency
4. **Model Quantization**: Use quantized models (4-bit or 8-bit) for faster inference

## Troubleshooting

### Common Issues

**Issue**: Model not loading
- **Solution**: Ensure you have enough RAM and the model path is correct

**Issue**: Slow performance
- **Solution**: Check if iGPU drivers are up to date and consider using a quantized model

**Issue**: Out of memory errors
- **Solution**: Reduce `max_memory` or `max_tokens` in configuration

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the open-source LLM community for making powerful models accessible
- Special thanks to the Qwen team for their excellent code-focused models
- Inspired by the need for private, local code assistance tools

## Contact

- **Author**: Xiping Yan
- **Repository**: [https://github.com/xipingyan/code_assistant](https://github.com/xipingyan/code_assistant)

## Roadmap

- [ ] Support for more LLM models
- [ ] Enhanced IDE integrations
- [ ] Web-based user interface
- [ ] Multi-language support for UI
- [ ] Performance benchmarking tools
- [ ] Docker containerization
- [ ] Cloud deployment options (optional)

---

**Note**: This project is under active development. Features and APIs may change.
