from __future__ import annotations

import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


def main() -> int:
    import flash_moe_mlx
    from scripts import run_qwen35, serve_openai

    assert hasattr(flash_moe_mlx, "load_model_bundle")
    parser = run_qwen35.build_arg_parser()
    assert parser.prog
    assert serve_openai.build_arg_parser().prog

    assembler = serve_openai.ResponseAssembler(stop_strings=["STOP"])
    for char in "<think>why</think>\n\nhello STOP dropped":
        assembler.push(char)
    assert assembler.reasoning == "why", assembler.reasoning
    assert assembler.content == "hello ", assembler.content
    assert assembler.stopped
    print("import-ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
