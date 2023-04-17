


<!-- =============== 2-05 질문 목록과 질문 상세 기능 만들기 부분에서 실습했던 코드 (이후에 쓰지 않는 코드) =============== -->
<!-- 질문 목록 -->
<!--{% if question_list %} ==> render_template 함수에서 전달받은 질문 목록 데이터 question_list가 있는지 검사한다.-->
<!--    <ul>-->
<!--    {% for question in question_list %} ==> question_list에 저장된 데이터를 하나씩 꺼내 question 객체에 대입한다. -->
                                             <!--   파이썬의 for~in 문을 떠올리면 쉽게 이해할 수 있을 것이다.-->

<!--        <li><a href="/detail/{{ question.id }}/">{{ question.subject }}</a></li>-->

<!--        =====================================================================================  -->
<!--        바로 앞의 for 문에서 얻은 question 객체의 id를 출력한다. -->
<!--        {{ question.subject }} 코드도 같은 맥락으로 이해할 수 있다-->
<!--        =====================================================================================  -->

<!--        2-05 하드 코딩된 URL에 url_for 함수 이용하기         -->
<!--        <li><a href="{{ url_for('question.detail', question_id=question.id) }}">{{ question.subject }}</a></li> -->

<!--        =====================================================================================  -->
<!--        기존에는 상세 페이지로 연결하는 링크가 /detail/{{ question.id }}/ 처럼 하드 코딩되어 있었다.
            이 부분을 url_for 함수를 이용해 question.detail 라우팅 함수로 URL을 찾도록 변경했다.
            이때 question.detail 함수는 question_id 매개변수가 필요하므로 question_id를 전달해야 한다. -->
<!--        =====================================================================================  -->

<!--    {% endfor %}-->
<!--    </ul>-->
<!--{% else %}-->
<!--    <p>질문이 없습니다.</p>-->
<!--{% endif %}-->


<!-- ======= 2-08 질문 목록에 부트스트랩 적용하기 부분에서 실습했던 코드 (기존의 코드(2-07이전의 코드) 전체를 수정) ======= -->
<!--<link rel="stylesheet" href="{{ url_for('static', filename='bootstrap.min.css') }}">-->
<!--<div class="container my-3">-->
<!--    <table class="table">-->
<!--        <thead>-->
<!--        <tr class="table-dark">-->
<!--            <th>번호</th>-->
<!--            <th>제목</th>-->
<!--            <th>작성일시</th>-->
<!--        </tr>-->
<!--        </thead>-->
<!--        <tbody>-->
<!--        {% if question_list %}-->
<!--        {% for question in question_list %}-->
<!--        <tr>-->
<!--            <td>{{ loop.index }}</td>-->
<!--            <td>-->
<!--                <a href="{{ url_for('question.detail', question_id=question.id) }}">{{ question.subject }}</a>-->
<!--            </td>-->
<!--            <td>{{ question.create_date }}</td>-->
<!--        </tr>-->
<!--        {% endfor %}-->
<!--        {% else %}-->
<!--        <tr>-->
<!--            <td colspan="3">질문이 없습니다.</td>-->
<!--        </tr>-->
<!--        {% endif %}-->
<!--        </tbody>-->
<!--    </table>-->

<!--    <a href="{{ url_for('question.create') }}" class="btn btn-primary">질문 등록하기</a> 2-10 폼 모듈로 데이터 검증 더 쉽게 하기 부분에서 추가되는 코드-->

<!--</div>-->