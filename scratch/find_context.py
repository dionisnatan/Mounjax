
import sys
import io

# Set stdout to utf-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def find_context(filename, search_str, context_size=500):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    start = 0
    while True:
        idx = content.find(search_str, start)
        if idx == -1:
            break
        
        ctx_start = max(0, idx - context_size)
        ctx_end = min(len(content), idx + len(search_str) + context_size)
        print(f"--- Occurrence at {idx} ---")
        print(content[ctx_start:ctx_end])
        print("-" * 30)
        start = idx + 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python find_context.py <search_str> [context_size]")
        sys.exit(1)
    
    search_str = sys.argv[1]
    context_size = int(sys.argv[2]) if len(sys.argv) > 2 else 500
    find_context('index.html', search_str, context_size)
