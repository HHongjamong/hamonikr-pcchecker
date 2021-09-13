# HamoniKR PC Checker

![GitHub
License](https://img.shields.io/github/license/2020-Invesum-Internship/hamonikr-pcchecker)
![GitHub repo
size](https://img.shields.io/github/repo-size/2020-Invesum-Internship/hamonikr-pcchecker)
![GitHub
contributors](https://img.shields.io/github/contributors/2020-Invesum-Internship/hamonikr-pcchecker)
![GitHub
stars](https://img.shields.io/github/stars/2020-Invesum-Internship/hamonikr-pcchecker?style=social)
![GitHub
forks](https://img.shields.io/github/forks/2020-Invesum-Internship/hamonikr-pcchecker?style=social)
![GitHub
issues](https://img.shields.io/github/issues/2020-Invesum-Internship/hamonikr-pcchecker?style=social)

‘HamoniKR PC Checker’ 는 한국의 일반 리눅스 데비안 계열의 OS 사용자들이  쉽게 보안상태를 점검/관리하고, 개인정보를 보호할 수 있도록 하는 보안 패널 서비스 입니다.
<br/>
[HamoniKR 3.0](https://hamonikr.org/), [TmaxOS OE](https://tmaxanc.com/#!/download/TmaxOSOE/product), [Gooroom](https://github.com/gooroom), [Hancom Gooroom](https://github.com/hancomgooroom), [Ubuntu](https://ubuntu.com/), [LinuxMint](https://linuxmint.com/) 에서의 호환성을 제공합니다.

PC Checker의 주요 기능은 다음과 같습니다.
* 시스템 점검 : PC의 여러가지 시스템 정보 및 점검항목들의 보안상태를 확인하고 각 점검항목을 설정합니다.
* 보안점검 알림 : 보안상태가 위험할 경우 알람 기능을 통해 사용자가 보안상태를 점검하도록 합니다.
* 개인 정보 보호 : PC 내 개인정보로 추정되는 데이터가 들어있는 파일을 찾고 해당되는 데이터에 대한 조치를 일괄적으로 수행합니다.

![스크린샷, 2021-09-09 01-36-12](https://user-images.githubusercontent.com/55476302/133084363-9a90c6dc-5af0-47d8-972c-a7a7f9b15dc7.png)
![스크린샷, 2021-09-05 19-00-43](https://user-images.githubusercontent.com/55476302/133084394-92a40717-cd64-4ea2-916e-c89f3e6ca0c0.png)

<br/>

## License

이 프로젝트는 [GPL3](./LICENSE) 을 따릅니다.

## HamoniKR PC Checker 설치

프로젝트의 [Release](https://github.com/HHongjamong/hamonikr-pcchecker/releases)에서 최신 패키지를 다운로드 받을 수 있습니다.

패키지를 다운로드 받은 후 다음 명령을 통해 설치합니다.
```
sudo apt install ./hamonikr-pcchecker-2.0.0_all.deb
```

## HamoniKR PC Checker 삭제

```
sudo apt purge hamonikr-pcchecker
```

## HamoniKR PC Checker 사용법

```
프로그램메뉴 > PC 지킴이 실행
```
보다 자세한 사용법은 [PC Checker 시연영상](https://www.youtube.com/watch?v=3maGiL3vSD8)을 통해 확인하실 수 있습니다.

## 소스코드 다운로드 및 빌드 방법

아래 명령어를 통해 소스코드를 다운로드 받고 빌드할 수 있습니다.
```
git clone https://github.com/HHongjamong/hamonikr-pcchecker.git && cd hamonikr-pcchecker

./build
```

## Contributing to HamoniKR PC Checker

이 프로젝트에 기여하는 방법은 다음과 같습니다.

1. 이 저장소를 Fork 하세요.
2. 자신이 작업할 branch 를 생성합니다 : `git checkout -b <branch_name>`.
3. 수정사항을 반영하고 커밋합니다 : `git commit -m '<commit_message>'`
4. 저장소에 작업한 브랜치를 Push : `git push origin hamonikr-pcchecker/<location>`
5. pull request 를 생성합니다.
* [여기](https://github.com/2020-Ocarina/hamonikr-pcchecker_source-packaging)서 소스 패키지를 확인하실 수 있습니다.

보다 자세한 내용은 GitHub documentation on [creating a pull
request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) 를 참고하세요.

## Contributors

이 프로젝트에 기여하신 기여자들:

* [@chaeya](https://github.com/chaeya) 📖
* [@Lukehan](https://github.com/LukeHan1128) 🐛
* [@yerin0130](https://github.com/yerin0130) 📖
* [@RyuSeohyeon16](https://github.com/RyuSeohyeon16) 🐛
* [@yeji0407](https://github.com/yeji0407) 📖

## Contact

연락이 필요한 경우 <yerin090989@gmail.com> 또는 <yejisoft@gmail.com> 로 내용을 보내주세요.  
프로젝트의 보다 자세한 사항과 모든 문서를 [해당 링크](http://team.hamonikr.org:18090/pages/viewpage.action?pageId=18415642)서 확인하실 수 있습니다.

