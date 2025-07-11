1. Run Wihtout Debugging vs Start Debugging
    - 두 실행 방법 모두 디버거를 사용하긴 하지만 디버깅 사용 가능 여부 차이가 존제
        - [stackoverflow](https://stackoverflow.com/questions/77452386/visual-studio-code-debugs-even-when-i-run-without-debugging)
    - [터미널 창의 유지/비유지 차이](https://storycompiler.tistory.com/208)
        - 디버거를 붙이지 않고 실행하면 터미널 창이 유지되고, 디버거를 붙이고 실행하면 터미널이 유지 되지 않는다.
2. flask 역할
    - 경량 WSGI 웹 어플리케이션 프레임워크
    - WSGI: Web Server Gateway Interface
        - 웹 서버가 어떻게 웹 어플리케이션과 통신하는 방식과 여러 웹 어플리케이션을 연결하여 요청을 처리하는 방식을 기술한 사양
        - [WSGI tutorial](https://wsgi.tutorial.codepoint.net/intro)
        - [PEP3333](https://peps.python.org/pep-3333/)
3. 0.0.0.0 설정 의미, 장단점
    - flask.run()의 host 매개변수는 수신할 IP 주소이다. 만약 0.0.0.0으로 설정한다면, 네트워크의 유저들이 서버에 접근할 수 있다.
    - 장점: 네트워크의 모든 유저가 서버에 접근 가능
    - 단점: 디버깅 모드에서 유저가 임의의 파이썬 코드를 실행 가능해서 보안적 문제가 있다.
4. 127.0.0.1 접속 vs 내부 IP 접속 차이
    - 127.0.0.1은 루프백 IP 주소로, 해당 컴퓨터 자체를 가리키는 특별한 주소이다. 네트워크 연결 없이도 컴퓨터 내부에서 통신이 가능하다.
    - 내부 IP인 10.0.x.x으로 접속한다면 원격 주소로 연결이 되어 같은 네트워크 상의 컴퓨터에서 접속 가능하다.
5. 포트 번호의 의미와 기본 충돌 시 해결 방안
    - 포트 번호는 어플리케이션이 네트워크를 통해 통신하기 위해 사용하는 번호이다.
    - 한 컴퓨터의 하나의 포트 번호에는 하나의 어플리케이션만이 지정될 수 있다.
    - 충돌 시 해결 방안
        - 하나의 포트에 하나의 어플리케이션만 지정한다.
            - 해당 port를 사용하는 어플리케이션을 찾아 종료
            - 다른 port를 사용
        - vm이나 container를 활용하여 내부적으로 사용한다.