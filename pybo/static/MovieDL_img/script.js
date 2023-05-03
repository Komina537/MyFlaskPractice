// span 요소 노드 가져오기
const spanEl = document.querySelector("main h2 span");
// 화면에 표시할 문장 배열
const txtArr = ['영화명을 입력하고 싶어진다', '배우를 입력하고 싶어진다', '장르를 선택하고 싶어진다', '예측 버튼을 누르고 싶어진다', '한번 더 검색하고 싶어진다'];
// 배열의 인덱스 초깃값
let index = 0;
// 화면에 표시할 문장 배열에서 요소를 하나 가져온 뒤, 배열로 만들기
let currentTxt = txtArr[index].split("");

// 텍스트 작성과 삭제 즉시 실행 함수 [ 형식 =>  (함수... 중략....)(); ]
(function(){
    const spanEl = document.querySelector("main h2 span");
    const txtArr = ['영화명을 입력하고 싶어진다', '배우를 입력하고 싶어진다', '장르를 선택하고 싶어진다', '예측 버튼을 누르고 싶어진다', '한번 더 검색하고 싶어진다'];
    let index = 0;
    let currentTxt = txtArr[index].split("");
    // 텍스트 입력 효과 구현하기
    function writeTxt(){
        spanEl.textContent += currentTxt.shift(); // ①
        if(currentTxt.length !== 0){ // ②
            setTimeout(writeTxt, Math.floor(Math.random() * 100));
        }else{ // ③
            currentTxt = spanEl.textContent.split("");
            setTimeout(deleteTxt, 3000);
        }
    }

    //텍스트 삭제 효과 구현하기
    function deleteTxt(){
        currentTxt.pop(); // ①
        spanEl.textContent = currentTxt.join("");// ②
        if(currentTxt.length !== 0){ // ③
            setTimeout(deleteTxt, Math.floor(Math.random() * 100));
        }else{ // ④
            index = (index + 1) % txtArr.length;
            currentTxt = txtArr[index].split("");
            writeTxt();
        }
    }
    writeTxt();
})();

function dp_menu(){
    let click = document.getElementById("drop-content");
    if(click.style.display === "none"){
        click.style.display = "block";

    }else{
        click.style.display = "none";

    }
}