from pathlib import Path
import secrets

# 修改了deeppavlov/core/utils


def get_download_token():
    token_file = Path.home() / '.deeppavlov'
    if not token_file.exists():
        token_file.write_text(secrets.token_urlsafe(32), encoding='utf8')

    # TODO:弱智路径死活不能转/ 直接用路径读
    # s = "/".join(str(token_file).split("\\"))
    f = open(str(token_file)+"\\token.txt", mode='r', encoding='utf8')

    return f.read().strip()
    # return token_file.read_text(encoding='utf8').strip()