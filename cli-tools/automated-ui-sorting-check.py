import subprocess
import sys
import os

def main():
    project_path = "projects/hacker-news-ui-tests"
    print(f"Running tests in: {project_path}\n")

    result = subprocess.run(
        [sys.executable, "-m", "pytest", project_path],
        cwd=os.getcwd(),
        stdout=sys.stdout,
        stderr=sys.stderr
    )

    if result.returncode == 0:
        print("\n✅ All tests passed.")
    else:
        print("\n❌ Some tests failed.")
        sys.exit(result.returncode)

if __name__ == "__main__":
    main()

Add CLI tool to run Hacker News UI tests
