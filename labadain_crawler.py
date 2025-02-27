import os
import subprocess
import argparse

#!/usr/bin/env python
#
# labadan_crawler.py
# Gabriel de Jesus (mestregabrieldejesus@gmail.com)
# Created on 27-02-2025


def create_essential_files():
    """Ensure the pipeline's required files exist."""
    base_path = "pipeline/data"
    file_names = ["domains.txt", "final_corpus.txt", "initial_corpus.txt",
                  "seed_words.txt", "stat_inlinks_outlinks.txt", "url_inlinks_outlinks.txt"]
    essential_files = [os.path.join(base_path, filename) for filename in file_names]

    # Ensure base directory exists““
    os.makedirs(base_path, exist_ok=True)
    for file in essential_files:
        if not os.path.exists(file):
            # Create an empty file
            open(file, 'w').close()


def run_seeder(iterations: int):
    """Run the seeder to generate seed words and URLs."""
    for i in range(1, iterations + 1):
        print(f"Generating seed words and seed URLs for the {i} time ...")
        subprocess.run(["python3", "./pipeline/seeder.py"], check=True)


def run_crawl(iterations: int):
    """Crawl the web to collect documents."""
    print("Crawling the World Wide Web ...")
    for i in range(1, iterations + 1):
        print(f"Crawling for the {i} time ...")
        subprocess.run(
            ["bash", "-c", f"cd nutch && ./bin/crawl -i -s urls/ --hostdbupdate --hostdbgenerate crawl/ {i} && cd .."], check=True)
    print("The crawling has been successfully concluded.")


def construct_corpus():
    """Build the target document collection."""
    print("Constructing text corpus ...")
    subprocess.run(["python3", "./pipeline/construct_corpus.py"], check=True)
    print("The corpus has been successfully generated.")


def generate_statistics():
    """Generate statistics for the collection."""
    print("Generating statistics for the collection ...")
    subprocess.run(["python3", "./pipeline/view_collection_stat.py"], check=True)
    print("The statistics have been successfully compiled.")


def main():
    parser = argparse.ArgumentParser(description="Labadain Crawler Pipeline")
    parser.add_argument("--seeder-runs", type=int, default=5, help="Number of times to run the seeder script")
    parser.add_argument("--crawl-runs", type=int, default=1, help="Number of times to run the crawl process")
    parser.add_argument("--skip-seeder", action="store_true", help="Skip running the seeder script")
    parser.add_argument("--skip-crawl", action="store_true", help="Skip the crawling process")
    parser.add_argument("--skip-corpus", action="store_true", help="Skip corpus construction")
    parser.add_argument("--skip-stats", action="store_true", help="Skip collection statistics generation")

    args = parser.parse_args()
    print(args)

    print("Initiating the crawling process ...")
    if not args.skip_seeder:
        run_seeder(args.seeder_runs)

    if not args.skip_crawl:
        run_crawl(args.crawl_runs)

    if not args.skip_corpus:
        construct_corpus()

    if not args.skip_stats:
        generate_statistics()


if __name__ == "__main__":
    create_essential_files()
    main()
