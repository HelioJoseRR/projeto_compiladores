# 🌐 Minipar Compiler - Web Interface

**Interactive web interface for the Minipar Compiler built with Gradio**

---

## 🚀 Quick Start

### Installation

```bash
# Install Gradio (only requirement)
pip install gradio

# OR install from requirements
pip install -r requirements.txt
```

### Run the Interface

```bash
# From the interface folder
cd interface
python app.py

# OR from project root
python interface\app.py
```

The interface will open automatically in your browser at `http://localhost:7860`

---

## ✨ Features

### 📝 Compiler Tab
- **Interactive Code Editor** - Write Minipar code with syntax highlighting
- **Example Programs** - Load pre-made examples instantly
- **Compilation Options** - Toggle different compilation stages:
  - 🔤 Show Tokens (Lexical Analysis)
  - 🌳 Show AST (Abstract Syntax Tree)
  - ✓ Show Semantic Analysis
  - 📝 Show TAC (Three-Address Code)
  - ⚙️ Show C Code
  - 🔧 Show Assembly Code
- **Compile Button** - See selected compilation stages
- **Download Button** - Generate and download `.exe` file directly

### ▶️ Execute Tab
- **Run Programs** - Execute code directly in browser
- **Input Support** - Provide input to programs
- **Real-time Output** - See program execution results
- **Example Programs** - Quick access to working examples

### ❓ Help Tab
- **Quick Start Guide** - Get started in minutes
- **Language Reference** - Complete syntax guide
- **Examples** - Code snippets for common patterns
- **Troubleshooting** - Common issues and solutions

---

## 🎯 Usage Examples

### Example 1: Compile and View TAC

1. Load "Loops" example from dropdown
2. Check "📝 Show TAC" option
3. Click "🔨 Compile"
4. View the three-address code output

### Example 2: Generate C Code

1. Write or load Minipar code
2. Check "⚙️ Show C Code" option
3. Click "🔨 Compile"
4. See the generated C source code

### Example 3: Download Executable

1. Write your program
2. Click "💾 Compile & Download .exe"
3. Download the executable file
4. Run it on your computer!

### Example 4: Execute Program

1. Go to "▶️ Execute" tab
2. Load "Factorial (Recursive)" example
3. Click "▶️ Execute Program"
4. See the output instantly

---

## 📁 File Structure

```
interface/
├── app.py              # Main Gradio interface
├── compiler_api.py     # Backend API wrapper
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

---

## 🔧 Architecture

### Frontend (app.py)
- Built with Gradio
- Provides interactive UI components
- Handles user interactions
- Manages tabs and display

### Backend (compiler_api.py)
- Wraps the Minipar compiler
- Provides clean API interface
- Handles compilation requests
- Manages file operations
- Executes programs safely

### Integration
```
User Input (Gradio)
       ↓
   app.py (UI)
       ↓
compiler_api.py (API)
       ↓
   compiler.py (Core)
       ↓
  Results (Display)
```

---

## 🎨 Interface Components

### Code Editor
- Syntax highlighting
- Line numbers
- Copy button
- Resizable

### Compilation Options (Checkboxes)
- ✅ Show Tokens
- ✅ Show AST
- ✅ Show Semantic Analysis
- ✅ Show TAC
- ✅ Show C Code
- ✅ Show Assembly

### Buttons
- **🔨 Compile** - Run compilation with selected options
- **💾 Compile & Download .exe** - Generate executable
- **▶️ Execute Program** - Run code directly

### Output Areas
- **Compilation Output** - Shows selected stages
- **Compilation Log** - Detailed compiler messages
- **Execution Output** - Program execution results
- **Download Area** - Get executable file

---

## 💡 Tips & Best Practices

### Writing Code
1. Start with example programs
2. Use print() for debugging
3. Check TAC to understand compilation
4. Test with Execute before downloading

### Compilation
1. Enable TAC for intermediate representation
2. Use C Code view to learn translation
3. Assembly view shows low-level code
4. Tokens view helps debug lexical errors

### Execution
1. Test programs in Execute tab first
2. Provide input in the input box
3. Programs have 10-second timeout
4. Check for infinite loops before running

### Debugging
1. Enable Tokens to check lexical analysis
2. Enable AST to verify syntax
3. Enable Semantic to catch type errors
4. Read compilation log for errors

---

## 🐛 Troubleshooting

### Interface Won't Start

**Problem:** `ModuleNotFoundError: No module named 'gradio'`

**Solution:**
```bash
pip install gradio
```

---

### Compilation Fails

**Problem:** Syntax or semantic errors

**Solution:**
1. Check error message in output
2. Enable Tokens to verify lexical analysis
3. Enable AST to check syntax
4. Review Help tab for syntax reference

---

### Download Doesn't Work

**Problem:** No file appears

**Solution:**
1. Ensure compilation succeeded (check output)
2. Look for error messages
3. Try compiling first, then download
4. Check browser download settings

---

### Execution Timeout

**Problem:** "Execution timeout (10 seconds)"

**Solution:**
1. Check for infinite loops
2. Reduce computation complexity
3. Test with smaller inputs
4. Download and run locally for long programs

---

### Display Issues

**Problem:** Output looks wrong or garbled

**Solution:**
1. Refresh the page
2. Try a different browser
3. Clear browser cache
4. Check console for errors (F12)

---

## 🔒 Security Notes

### Safe Execution
- Programs run in isolated process
- 10-second execution timeout
- Temporary files cleaned up
- No network access from compiled code

### Limitations
- Cannot execute programs requiring files
- No persistent storage
- Limited to single-file programs
- Windows executables only (currently)

---

## 🚀 Advanced Usage

### Custom Examples

Add your own examples by editing `EXAMPLES` dict in `app.py`:

```python
EXAMPLES = {
    "My Example": """# Your code here
print("Hello!")
""",
    # ... more examples
}
```

### API Integration

Use the API directly in your code:

```python
from compiler_api import CompilerAPI

api = CompilerAPI()
result = api.compile_code(
    source_code="print('Hello')",
    show_tac=True,
    generate_exe=True
)

print(result['tac'])
```

### Port Configuration

Change the port in `app.py`:

```python
app.launch(
    server_port=8080,  # Your custom port
    share=False
)
```

### Share Online

Enable sharing to get public URL:

```python
app.launch(
    share=True  # Creates public link
)
```

---

## 📊 Performance

### Compilation Speed
- Lexical Analysis: < 0.1s
- Parsing: < 0.1s
- Semantic Analysis: < 0.1s
- Code Generation: < 0.1s
- C Generation: < 0.1s
- GCC Compilation: 1-3s

**Total:** ~3-5 seconds for full compilation

### Execution Speed
- Program startup: < 1s
- Execution: Depends on program
- Timeout: 10 seconds maximum

---

## 🎓 Learning Resources

### Tutorials
1. Start with "Hello World" example
2. Try "Variables and Arithmetic"
3. Learn "Functions" example
4. Explore "Loops" and "Conditionals"
5. Master "Factorial" (recursion)

### Documentation
- **Help Tab** - Quick reference in interface
- **COMPLETE_GUIDE.md** - Comprehensive guide (project root)
- **README.md** - Project overview (project root)
- **docs/tutorials/** - Detailed tutorials

---

## 🛠️ Development

### Running in Development Mode

```bash
# Enable auto-reload
python app.py --reload

# Enable debug mode
python app.py --debug
```

### Customizing the Interface

Edit `app.py`:
- Modify `custom_css` for styling
- Update `EXAMPLES` for different examples
- Change layout in Gradio blocks
- Add new tabs or features

### Testing the API

```python
# Test compilation
from compiler_api import compile_and_show

result = compile_and_show(
    "print('Test')",
    show_tokens=True,
    show_tac=True
)
print(result)
```

---

## 📝 Example Workflow

### Complete Development Cycle

1. **Write Code**
   - Open interface
   - Load "Functions" example
   - Modify to add your function

2. **Debug**
   - Enable Tokens and AST
   - Click Compile
   - Check for errors

3. **Analyze**
   - Enable TAC view
   - Study intermediate code
   - Understand compilation

4. **Test**
   - Go to Execute tab
   - Run program
   - Verify output

5. **Deploy**
   - Click Download .exe
   - Get executable
   - Share with others!

---

## 🌟 Features Comparison

### Web Interface vs Command Line

| Feature | Web Interface | Command Line |
|---------|--------------|--------------|
| Code Editor | ✅ Visual | ❌ External editor |
| Multiple Views | ✅ Tabs | ❌ Multiple commands |
| Examples | ✅ Dropdown | ❌ Manual |
| Execution | ✅ In-browser | ✅ Terminal |
| Download | ✅ One click | ❌ Find file |
| Help | ✅ Built-in | ❌ External docs |
| Accessibility | ✅ Any device | ❌ Terminal only |

**Both are fully functional!** Choose based on preference.

---

## 🤝 Contributing

Want to improve the interface?

1. Edit `app.py` for UI changes
2. Edit `compiler_api.py` for API changes
3. Add examples to EXAMPLES dict
4. Improve CSS styling
5. Add new features or tabs

---

## 📞 Support

### Getting Help

1. Check Help tab in interface
2. Read COMPLETE_GUIDE.md
3. Review examples
4. Check troubleshooting section

### Common Questions

**Q: Can I use this offline?**
A: Yes! Runs completely locally.

**Q: Does it work on mobile?**
A: Yes! Interface is responsive.

**Q: Can I share my programs?**
A: Yes! Download .exe or share code.

**Q: Is my code saved?**
A: No, code is temporary. Save manually.

---

## 🎉 Summary

The Minipar Web Interface provides:

✅ **Easy to use** - No command line needed
✅ **Visual** - See all compilation stages
✅ **Interactive** - Edit and test instantly
✅ **Educational** - Learn compiler internals
✅ **Powerful** - Full compiler features
✅ **Accessible** - Works anywhere

**Start coding now!** Just run `python app.py` 🚀

---

**Version:** 1.0
**Last Updated:** January 2025
**Status:** ✅ Production Ready
**Built With:** Gradio, Python
**License:** Educational Use
