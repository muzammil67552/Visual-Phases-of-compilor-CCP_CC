import tkinter as tk
from tkinter import scrolledtext
import re

# ----- TOKEN CLASS -----
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    def __repr__(self):
        return f"{self.type}({self.value})"

# ----- STATE MACHINE -----
class StateMachine:
    def __init__(self):
        self.state = 'START'

    def process(self, token):
        if self.state == 'START':
            if token.type == 'ID' or token.type == 'KEYWORD':
                self.state = 'ID_SEEN'
            elif token.type == 'NUMBER':
                self.state = 'NUMBER_SEEN'
            else:
                self.state = 'ERROR'
        elif self.state in ['ID_SEEN', 'NUMBER_SEEN']:
            if token.type == 'OP':
                self.state = 'OP_SEEN'
            elif token.type == 'EQUALS':
                self.state = 'EQUALS_SEEN'
            else:
                self.state = 'ERROR'
        elif self.state == 'OP_SEEN':
            if token.type in ['ID', 'NUMBER', 'KEYWORD']:
                self.state = 'EXPR_COMPLETE'
            else:
                self.state = 'ERROR'
        elif self.state == 'EQUALS_SEEN':
            if token.type in ['ID', 'NUMBER']:
                self.state = 'EXPR_COMPLETE'
            else:
                self.state = 'ERROR'
        return self.state

# ----- LEXER -----
class Lexer:
    KEYWORDS = {'likho', 'adda', 'jama', 'ghata'}

    def __init__(self, text):
        self.text = text
        self.tokens = []

    def tokenize(self):
        token_spec = [
            ('NUMBER',   r'\d+'),
            ('ID',       r'[A-Za-z_][A-Za-z0-9_]*'),
            ('OP',       r'[+\-*/]'),
            ('EQUALS',   r'='),
            ('SKIP',     r'[ \t]+'),
            ('MISMATCH', r'.')
        ]
        token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_spec)
        self.tokens = []

        for match in re.finditer(token_regex, self.text):
            kind = match.lastgroup
            value = match.group()
            if kind == 'SKIP':
                continue
            elif kind == 'MISMATCH':
                raise RuntimeError(f"Unexpected character: {value}")
            elif kind == 'ID' and value in self.KEYWORDS:
                kind = 'KEYWORD'  # Keywords کو الگ classify کریں
            self.tokens.append(Token(kind, value))
        return self.tokens

# ----- PARSER -----
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        if not self.tokens:
            raise SyntaxError("Empty input")
        tree = self.expr()
        if self.pos < len(self.tokens):
            raise SyntaxError(f"Unexpected token: {self.tokens[self.pos]}")
        return "Syntax OK \u2705", tree

    def expr(self):
        node = self.term()
        while self.pos < len(self.tokens) and self.tokens[self.pos].type == 'OP':
            op = self.tokens[self.pos]
            self.pos += 1
            right = self.term()
            node = ('Expr', node, op, right)
        return node

    def term(self):
        token = self.tokens[self.pos]
        if token.type in ('ID', 'NUMBER', 'KEYWORD'):
            self.pos += 1
            return token
        else:
            raise SyntaxError(f"Invalid token: {token}")

# ----- SEMANTIC ANALYZER -----
class SemanticAnalyzer:
    def __init__(self, tree):
        self.tree = tree

    def analyze(self):
        # آپ چاہیں تو semantic rules یہاں ڈال سکتے ہیں، ابھی سادہ "OK" واپس کر رہا ہے۔
        return "Semantic OK \u2705"

# ----- GUI LOGIC -----
class CompilerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("\ud83d\udcbb CompileX: Visual Compiler Phases")
        self.root.geometry("850x700")
        self.root.configure(bg="#f2f4f8")

        self.build_ui()

    def build_ui(self):
        # Heading
        heading = tk.Label(self.root, text="CompileX: Visual Compiler Phases", font=("Arial", 22, "bold"), bg="#f2f4f8", fg="#2c3e50")
        heading.pack(pady=10)

        # Input Entry
        self.entry = tk.Entry(self.root, font=("Consolas", 14), width=70)
        self.entry.pack(pady=10)

        # Buttons Frame
        btn_frame = tk.Frame(self.root, bg="#f2f4f8")
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Lexical", command=self.lexical, bg="#0984e3", fg="white", padx=10, pady=5).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Syntax", command=self.syntax, bg="#00cec9", fg="black", padx=10, pady=5).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Semantic", command=self.semantic, bg="#fd79a8", fg="black", padx=10, pady=5).grid(row=0, column=2, padx=10)
        tk.Button(btn_frame, text="State Machine", command=self.state_machine, bg="#ffeaa7", fg="black", padx=10, pady=5).grid(row=0, column=3, padx=10)

        # Sample Programs Dropdown
        sample_label = tk.Label(self.root, text="Sample Programs:", bg="#f2f4f8")
        sample_label.pack(pady=(10,0))

        self.sample_var = tk.StringVar()
        self.sample_menu = tk.OptionMenu(self.root, self.sample_var,
                                         "adda x = 5",
                                         "likho x jama 3",
                                         "adda y = 10",
                                         "likho y ghata 2",
                                         "likho 5 jama 5")
        self.sample_menu.pack()
        self.sample_var.set("adda x = 5")

        load_btn = tk.Button(self.root, text="Load Sample", command=self.load_sample)
        load_btn.pack(pady=5)

        # Output Text Area
        self.output = scrolledtext.ScrolledText(self.root, height=22, font=("Consolas", 12), bg="white", fg="black", wrap=tk.WORD)
        self.output.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Grammar Documentation as comment (آپ چاہیں تو report میں بھی شامل کریں)
        grammar_text = """
        Grammar Rules (BNF):
        program       ::= statement_list
        statement_list ::= statement | statement statement_list
        statement     ::= 'adda' ID '=' expr | 'likho' expr
        expr          ::= term { ('jama' | 'ghata') term }
        term          ::= ID | NUMBER
        ID            ::= [a-zA-Z_][a-zA-Z0-9_]*
        NUMBER        ::= [0-9]+
        """
        print(grammar_text)  # آپ چاہیں تو اس کو GUI میں بھی دکھا سکتے ہیں

    def load_sample(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.sample_var.get())

    def show_result(self, result, color="black"):
        self.output.configure(state="normal")
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, result)
        self.output.tag_add("result", "1.0", "end")
        self.output.tag_config("result", foreground=color)
        self.output.configure(state="disabled")

    def lexical(self):
        try:
            lexer = Lexer(self.entry.get())
            tokens = lexer.tokenize()
            formatted = '\n'.join([str(t) for t in tokens])
            self.show_result(f"\ud83d\udd39 Tokens:\n{formatted}", "blue")
        except Exception as e:
            self.show_result(f"Lexical Error \u274c: {str(e)}", "red")

    def syntax(self):
        try:
            lexer = Lexer(self.entry.get())
            tokens = lexer.tokenize()
            parser = Parser(tokens)
            result, tree = parser.parse()
            self.show_result(f"\ud83e\udde9 {result}", "green")
        except Exception as e:
            self.show_result(f"Syntax Error \u274c: {str(e)}", "red")

    def semantic(self):
        try:
            lexer = Lexer(self.entry.get())
            tokens = lexer.tokenize()
            parser = Parser(tokens)
            _, tree = parser.parse()
            semantic = SemanticAnalyzer(tree)
            result = semantic.analyze()
            self.show_result(f"\u2705 {result}\n\n\ud83e\udde0 Parse Tree:\n{tree}", "purple")
        except Exception as e:
            self.show_result(f"Semantic Error \u274c: {str(e)}", "red")

    def state_machine(self):
        try:
            lexer = Lexer(self.entry.get())
            tokens = lexer.tokenize()
            sm = StateMachine()
            trace = []
            for token in tokens:
                state = sm.process(token)
                trace.append(f"Token: {token} \t=> State: {state}")
            self.show_result("\ud83c\udf10 State Machine Trace:\n" + '\n'.join(trace), "orange")
        except Exception as e:
            self.show_result(f"State Machine Error \u274c: {str(e)}", "red")

# ----- MAIN -----
if __name__ == "__main__":
    root = tk.Tk()
    app = CompilerGUI(root)
    root.mainloop()
