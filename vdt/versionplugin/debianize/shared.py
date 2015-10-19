import argparse

def parse_version_extra_args(version_args):
    p = argparse.ArgumentParser(description="Package python packages with debianize.sh.")
    p.add_argument('--include','-i', action='append', help="Using this flag makes following dependencies explicit. It will only build dependencies listed in install_requires that match the regex specified after -i. Use -i multiple times to specify multiple packages")
    p.add_argument('--exclude', '-I', action='append', help="Using this flag, packages can be exluded from being built, dependencies matching the regex, whill not be built")
    args, extra_args = p.parse_known_args(version_args)
    
    return args, extra_args
    