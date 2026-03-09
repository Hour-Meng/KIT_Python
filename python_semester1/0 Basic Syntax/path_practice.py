from pathlib import Path
import os


def main() -> None:
    # 1) Current working directory (changes based on how you launch Python)
    cwd = Path.cwd()

    # 2) This script file and folder (stable)
    script_file = Path(__file__).resolve()
    script_dir = script_file.parent

    # 3) Build a script-relative path to your basketball game image
    img_script_relative = script_dir.parent / "9.basket_ball_game" / "basketball_bg.gif"

    # 4) Relative path from current working directory
    img_relative = Path("python_semester1/9.basket_ball_game/basketball_bg.gif")

    # 5) Home-relative example (~) expanded to absolute
    home_docs = Path("~/Documents").expanduser().resolve()

    print("=== Path Practice ===")
    print(f"Current working directory (cwd): {cwd}")
    print(f"Script file (__file__):          {script_file}")
    print(f"Script directory:                {script_dir}")
    print()

    print("--- Absolute vs Relative ---")
    print(f"Relative image path:            {img_relative}")
    print(f"Resolved from cwd:              {img_relative.resolve()}")
    print(f"Script-relative image path:     {img_script_relative}")
    print()

    print("--- Exists? ---")
    print(f"Relative exists from cwd:       {img_relative.exists()}")
    print(f"Script-relative exists:         {img_script_relative.exists()}")
    print()

    print("--- Other path styles ---")
    print(f"Home shortcut (~) expanded:     {home_docs}")
    print(f"Parent folder of script:        {script_dir.parent}")
    print(f"Current folder symbol '.':      {Path('.').resolve()}")
    print(f"Parent symbol '..':             {Path('..').resolve()}")


if __name__ == "__main__":
    main()
