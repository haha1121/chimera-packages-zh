pkgname = "fonts-harmonyos-sans"
pkgver = "1.0"
pkgrel = 0
pkgdesc = "HarmonyOS-Sans font-family"
maintainer = "Amigdal <haha112145@163.com>"
license = "OFL-1.1"
url = "https://developer.harmonyos.com"
source = f"{url}/resource/image/design/resource/download/general/HarmonyOS-Sans.zip"
sha256 = "fb02c86e358cd9aad8d4dfa957ee502381e7ee2e94499a9133add4324b6ce69a"


def do_install(self):
    for f in (self.cwd / "HarmonyOS Sans/HarmonyOS_Sans*").glob("*.ttf"):
        self.install_file(f, "usr/share/fonts/harmonyos-sans")
