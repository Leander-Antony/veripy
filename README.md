# VeriPy 🔍

A comprehensive fact-checking system that combines machine learning predictions with real-time web verification to assess the truthfulness of claims and statements.

## 🌟 Overview

VeriPy is a multi-layered fact-checking application that leverages:
- **Machine Learning**: Pre-trained Naive Bayes model for initial classification
- **Web Search Integration**: Real-time verification using Google Search and web scraping
- **LLM Analysis**: Ollama-powered natural language processing for comprehensive reports
- **Web Interface**: Clean, responsive Flask web application
- **Browser Extension**: Chrome extension for seamless text verification

## 🏗️ Architecture

The system operates through three distinct layers:

### Layer 1: ML Classification (`utils/layer1.py`)
- Uses a pre-trained Naive Bayes model to classify text
- Utilizes CountVectorizer for text preprocessing
- Provides initial label prediction for incoming claims

### Layer 2: Web Verification (`utils/layer2.py`)
- Performs Google searches for claim verification
- Scrapes web content using BeautifulSoup
- Uses Ollama LLM (Llama3) to analyze search results
- Generates confidence scores and verdicts

### Layer 3: Report Generation (`utils/layer3.py`)
- Combines ML predictions with web verification results
- Generates comprehensive fact-checking reports
- Provides final confidence scores and source links

## 🚀 Features

- **Real-time Fact Checking**: Instant verification of claims and statements
- **Multi-source Verification**: Combines ML models with live web data
- **Confidence Scoring**: Numerical confidence ratings for reliability assessment
- **Source Attribution**: Links to relevant sources supporting the verification
- **Clean Web Interface**: Modern, responsive UI with dark theme
- **Browser Extension**: Quick fact-checking directly from web pages
- **Session Management**: Persistent results during user sessions

## 📁 Project Structure

```
veripy/
├── app.py                      # Main Flask application
├── test.py                     # Testing utilities
├── utils/                      # Core verification modules
│   ├── layer1.py              # ML classification layer
│   ├── layer2.py              # Web verification layer
│   ├── layer3.py              # Report generation layer
│   └── model/                 # Pre-trained ML models
│       ├── count_vectorizer.pkl
│       ├── label_encoder.pkl
│       └── naive_bayes_model.pkl
├── train/                      # Model training components
│   ├── train.py               # Model training script
│   ├── predict.py             # Prediction utilities
│   ├── train_fixed.tsv        # Training dataset
│   └── *.pkl                  # Trained model files
├── templates/
│   └── index.html             # Main web interface
├── static/                    # Static assets
├── extension/                 # Chrome extension
│   ├── manifest.json          # Extension configuration
│   ├── background.js          # Extension background script
│   ├── content.js             # Content script
│   ├── body.js                # UI components
│   ├── body.css               # Extension styling
│   ├── index.html             # Extension popup
│   └── icons/                 # Extension icons
└── README.md                  # This file
```

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Ollama with Llama3 model installed
- Chrome browser (for extension)

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/veripy.git
   cd veripy
   ```

2. **Install Python dependencies**
   ```bash
   pip install flask langchain-community duckduckgo-search googlesearch-python requests beautifulsoup4 scikit-learn pandas ollama
   ```

3. **Install and setup Ollama**
   ```bash
   # Install Ollama (visit https://ollama.ai for installation instructions)
   ollama pull llama3
   ```

4. **Verify model files**
   Ensure the pre-trained models are in `utils/model/`:
   - `count_vectorizer.pkl`
   - `label_encoder.pkl` 
   - `naive_bayes_model.pkl`

## 🚦 Usage

### Web Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:5000`

3. **Enter a claim**
   Type any statement or claim you want to fact-check

4. **Review results**
   - View the confidence score
   - Read the comprehensive report
   - Check source links for verification

### Browser Extension

1. **Load the extension**
   - Open Chrome and go to `chrome://extensions/`
   - Enable "Developer mode"
   - Click "Load unpacked" and select the `extension/` folder

2. **Use the extension**
   - Select text on any webpage
   - Right-click and choose the VeriPy option
   - View fact-checking results

### Training New Models

To retrain the ML model with new data:

```bash
cd train/
python train.py
```

## 🔧 Configuration

### Ollama Model
The system uses Llama3 by default. To change the model, edit the `model` parameter in:
- `utils/layer2.py` (line 9)
- `utils/layer3.py` (line 18)

### Search Configuration
Modify search parameters in `utils/layer2.py`:
- `max_results`: Number of search results to analyze
- Search providers: Currently supports Google Search

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📋 API Reference

### Core Functions

#### `layer1.predict_label(text)`
- **Input**: Text string to classify
- **Output**: Predicted label from ML model

#### `layer2.fact_check(statement)`
- **Input**: Statement to fact-check
- **Output**: Tuple of (verdict, sources)

#### `layer3.generate_combined_report(statement)`
- **Input**: Statement to analyze
- **Output**: Dictionary with score, links, and report

### Flask Routes

- `GET/POST /`: Main interface for fact-checking
- `GET /reset`: Clear session data

## 🐛 Troubleshooting

### Common Issues

1. **Ollama not responding**
   - Ensure Ollama service is running
   - Verify Llama3 model is downloaded

2. **Model files missing**
   - Check `utils/model/` directory
   - Retrain models using `train/train.py`

3. **Search results empty**
   - Check internet connection
   - Verify Google Search API limits

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Ollama** for local LLM capabilities
- **scikit-learn** for machine learning tools
- **Flask** for web framework
- **BeautifulSoup** for web scraping
- **LangChain** for LLM integration

## 📈 Future Enhancements

- [ ] Support for multiple LLM providers
- [ ] Enhanced browser extension features
- [ ] API endpoints for external integration
- [ ] Advanced caching mechanisms
- [ ] Multi-language support
- [ ] Real-time fact-checking dashboard
- [ ] Integration with social media platforms

---

**Built with ❤️ for truth and transparency**