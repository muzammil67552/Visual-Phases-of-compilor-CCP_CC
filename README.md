# 🖥️ CompileX: Visual Compiler Phases

**An Intuitive Desktop App to Simulate and Visualize Lexical, Syntax, and Semantic Analysis in Real-Time Using Python**

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Grammar Rules](#grammar-rules)
- [Project Structure](#project-structure)
- [Technical Implementation](#technical-implementation)
- [Sample Programs](#sample-programs)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

CompileX is an educational desktop application that provides real-time visualization of compiler phases including **Lexical Analysis**, **Syntax Analysis**, **Semantic Analysis**, and **State Machine** processing. Built with Python and Tkinter, it offers an intuitive interface for students and educators to understand how compilers work internally.

### 🎓 Educational Purpose
This project serves as a practical learning tool for:
- Computer Science students studying compiler design
- Educators teaching compiler construction courses
- Developers interested in understanding compilation processes
- Anyone curious about how programming languages are processed

## ✨ Features

### 🔍 **Lexical Analysis (Tokenization)**
- Real-time tokenization of input code
- Recognition of keywords, identifiers, numbers, and operators
- Custom token classification with visual feedback
- Error detection for invalid characters

### 🌳 **Syntax Analysis (Parsing)**
- Recursive descent parser implementation
- Parse tree generation and visualization
- Grammar rule validation
- Comprehensive syntax error reporting

### 🧠 **Semantic Analysis**
- Semantic rule checking
- Parse tree analysis
- Type checking foundation
- Semantic error detection

### 🔄 **State Machine Visualization**
- Step-by-step state transitions
- Token processing trace
- Visual state flow representation
- Interactive debugging capability

### 🎨 **User Interface**
- Clean, modern GUI design
- Color-coded output for different phases
- Sample program library
- Real-time processing and feedback

## 🖼️ Screenshots

*Add screenshots of your application here showing different compiler phases in action*

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- Tkinter (usually comes with Python)

### Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/muzammil67552/Visual-Phases-of-compilor-CCP_CC.git
   cd compiler_gui.py
   ```

2. **Run the application**
   ```bash
   python compiler_gui.py
   ```

No additional dependencies required! The application uses only Python standard library.

## 📖 Usage

### Getting Started
1. Launch the application by running `compiler_gui.py`
2. Enter your code in the input field or select a sample program
3. Click on any phase button to see the analysis:
   - **Lexical**: View tokenization results
   - **Syntax**: Check grammar compliance and see parse trees
   - **Semantic**: Perform semantic analysis
   - **State Machine**: Trace state transitions

### Sample Programs
The application includes several pre-built sample programs:
- `adda x = 5` - Variable assignment
- `likho x jama 3` - Expression with addition
- `adda y = 10` - Another assignment
- `likho y ghata 2` - Expression with subtraction
- `likho 5 jama 5` - Simple arithmetic

## 📝 Grammar Rules

The compiler supports a custom language with the following BNF grammar:

```bnf
program       ::= statement_list
statement_list ::= statement | statement statement_list
statement     ::= 'adda' ID '=' expr | 'likho' expr
expr          ::= term { ('jama' | 'ghata') term }
term          ::= ID | NUMBER
ID            ::= [a-zA-Z_][a-zA-Z0-9_]*
NUMBER        ::= [0-9]+
```

### Keywords
- `adda` - Variable declaration/assignment
- `likho` - Print/output statement
- `jama` - Addition operator
- `ghata` - Subtraction operator

## 🏗️ Project Structure

```
CC Project/
│
├── compiler_gui.py          # Main application file
├── README.md               # Project documentation
└── screenshots/            # Application screenshots (optional)
```

## 🔧 Technical Implementation

### Core Components

#### 1. **Token Class**
```python
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
```
Represents individual tokens with type and value attributes.

#### 2. **Lexer Class**
- Implements regular expression-based tokenization
- Handles keyword recognition
- Provides error handling for invalid characters

#### 3. **Parser Class**
- Recursive descent parser implementation
- Generates parse trees
- Comprehensive syntax error reporting

#### 4. **State Machine Class**
- Tracks parsing states
- Provides step-by-step execution trace
- Visual representation of state transitions

#### 5. **Semantic Analyzer Class**
- Foundation for semantic rule checking
- Parse tree analysis capabilities
- Extensible for advanced semantic features

### GUI Architecture
- **Tkinter-based** interface for cross-platform compatibility
- **Event-driven** programming model
- **Modular design** for easy maintenance and extension

## 🧪 Sample Programs

### Basic Assignment
```
adda x = 5
```
**Output**: Demonstrates variable assignment tokenization and parsing.

### Arithmetic Expression
```
likho x jama 3
```
**Output**: Shows expression parsing with addition operator.

### Complex Expression
```
likho 5 jama 5
```
**Output**: Illustrates numeric literal processing and arithmetic operations.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Areas for Contribution
- Additional language features
- Enhanced error reporting
- More visualization options
- Performance optimizations
- Documentation improvements

## 📚 Educational Value

This project demonstrates:
- **Compiler Design Principles**: Practical implementation of compilation phases
- **GUI Development**: Modern desktop application design with Python
- **Software Architecture**: Clean, modular code organization
- **Error Handling**: Comprehensive error detection and reporting
- **Regular Expressions**: Pattern matching for tokenization
- **Recursive Algorithms**: Parser implementation using recursion

## 🔮 Future Enhancements

- [ ] Code generation phase
- [ ] Symbol table management
- [ ] More programming language constructs
- [ ] Syntax highlighting in input
- [ ] Export functionality for parse trees
- [ ] Interactive grammar editing
- [ ] Performance metrics display

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Inspired by compiler design courses and textbooks
- Built for educational purposes to help students understand compiler construction
- Thanks to the Python and Tkinter communities for excellent documentation

---

⭐ **Star this repository if you found it helpful!**

*Made with ❤️ for the programming education community*