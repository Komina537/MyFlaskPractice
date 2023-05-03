
const model1 = await tf.loadLayersModel('http://127.0.0.1:5500/reg/model.json');
const model2 = await tf.loadLayersModel('http://127.0.0.1:5500/cls/model.json');
let inputData1;
let outputData1;
let inputData2;
let outputData2;
let output1;
let output2;
let dir_score;
let actors_score = 0;
let film_score;
let jsondata;

let total_people = [{ 2018: 0.01883919 }, { 2009: -0.85400814 }, { 2022: -1.463612 }, { 2017: 0.06880218 }, { 2013: -0.02458718 }, { 2015: 0.0319241 },
{ 2010: -0.96334467 }, { 2019: 0.16616104 }, { 2012: -0.28879513 }, { 2020: -2.22617752 }, { 2016: 0.02801201 }, { 2011: -0.79209665 }, { 2021: -2.2117635 }, { 2008: -0.9680759 }, { 2014: 0 }, { 2023: -1.463612 }]

// inputData = tf.tensor2d([[2, 2, 0, -1.463612, 0, 17, 1, -0.308725, 0]]);
// outputData = model.predict(inputData);
// output = outputData.dataSync();
// console.log(output[0])


fetch("movie_top_300.json")
    .then(response => response.json())
    .then(data => {
        jsondata = data;
    });
document.getElementsByTagName('form')[0].onsubmit = function () {
    let movie_name = document.getElementById('movie_name');
    let genre = document.getElementById('genre');
    let film_rating = document.getElementById('film_rating');
    let director = document.getElementById('director');
    let actors = document.getElementById('actors');
    let distributor = document.getElementById('distributor');
    let year = document.getElementById('year');
    let screen = document.getElementById('screen');
    let total;
    let screen_scaled = (screen.value - 166) / (257 - 108)
    let co;
    let season;
    let year2;

    actors_score = 0;

    if ((2020 <= year.value.slice(0, 4)) && (year.value.slice(0, 4) <= 2022)) {
        co = 1;
    }
    else co = 0;
    for (let i = 0; i < total_people.length; i++) {
        if (total_people[i][year.value.slice(0, 4)]) {
            total = total_people[i][year.value.slice(0, 4)];
        }
    }

    for (let i = 0; i < 300; i++) {
        if (jsondata[i]['감독'] == director.value && jsondata[i]['개봉일'] < year.value) {
            if (i >= 271) dir_score = 1;
            else if (i >= 241) dir_score = 2;
            else if (i >= 211) dir_score = 3;
            else if (i >= 181) dir_score = 4;
            else if (i >= 151) dir_score = 5;
            else if (i >= 121) dir_score = 6;
            else if (i >= 91) dir_score = 7;
            else if (i >= 61) dir_score = 8;
            else if (i >= 31) dir_score = 9;
            else dir_score = 10;
        }
        else dir_score = 0;
    }
    let arr2 = (actors.value).split(',');
    for (let i = 0; i < 300; i++) {
        let arr = (jsondata[i]['출연']).slice(2, -2).split("\', \'");
        for (let j = 0; j < arr.length; j++) {
            for (let k = 0; k < arr2.length; k++) {
                if (arr[j] == arr2[k] && jsondata[i]['개봉일'] < year.value) {
                    if (i >= 271) actors_score += 1;
                    else if (i >= 241) actors_score += 2;
                    else if (i >= 211) actors_score += 3;
                    else if (i >= 181) actors_score += 4;
                    else if (i >= 151) actors_score += 5;
                    else if (i >= 121) actors_score += 6;
                    else if (i >= 91) actors_score += 7;
                    else if (i >= 61) actors_score += 8;
                    else if (i >= 31) actors_score += 9;
                    else actors_score += 10;
                }
            }
        }
    }
    for (let i = 0; i < 300; i++) {
        if (jsondata[i]['배급사'] == distributor.value && jsondata[i]['개봉일'] < year.value) {
            if (i >= 271) film_score = 1;
            else if (i >= 241) film_score = 2;
            else if (i >= 211) film_score = 3;
            else if (i >= 181) film_score = 4;
            else if (i >= 151) film_score = 5;
            else if (i >= 121) film_score = 6;
            else if (i >= 91) film_score = 7;
            else if (i >= 61) film_score = 8;
            else if (i >= 31) film_score = 9;
            else film_score = 10;
        }
        else film_score = 0;
    }
    switch (Number(year.value.slice(5, 7))) {
        case 1:
        case 2:
            season = 1;
            break;
        case 3:
        case 4:
        case 5:
            season = 2;
            break;
        case 6:
        case 7:
        case 8:
            season = 3;
            break;
        case 9:
        case 10:
        case 11:
            season = 0;
            break;
        case 12:
            season = 1;
        default:
            break;
    }
    switch (Number(year.value.slice(0, 4))) {
        case 2014:
            year2 = 7;
            break;
        case 2019:
            year2 = 12;
            break;
        case 2017:
            year2 = 10;
            break;
        case 2009:
            year2 = 2;
            break;
        case 2015:
            year2 = 8;
            break;
        case 2012:
            year2 = 5;
            break;
        case 2013:
            year2 = 6;
            break;
        case 2022:
            year2 = 15;
            break;
        case 2018:
            year2 = 11;
            break;
        case 2016:
            year2 = 9;
            break;
        case 2008:
            year2 = 1;
            break;
        case 2011:
            year2 = 4;
            break;
        case 2021:
            year2 = 14;
            break;
        case 2010:
            year2 = 3;
            break;
        case 2020:
            year2 = 13;
            break;
        case 2007:
            year2 = 0;
            break;
        case 2023:
            year2 = 16;
            break;

    }
    inputData1 = tf.tensor2d([[Number(genre.value), Number(film_rating.value), dir_score, Number(total), film_score, actors_score, season, screen_scaled, co]]);
    outputData1 = model1.predict(inputData1);
    output1 = outputData1.dataSync();

    inputData2 = tf.tensor2d([[Number(genre.value), Number(film_rating.value), dir_score, Number(total), film_score, actors_score, season, screen_scaled, year2, co]]);
    outputData2 = model2.predict(inputData2);
    output2 = outputData2.dataSync();
    return false;
}
document.getElementById("reg_btn").onclick = () => {

    if (document.getElementById('result')) {
        document.getElementById('result').remove(document.getElementById('result'));
    }

    const newDivEl = document.createElement('div');
    newDivEl.setAttribute('id', 'result');
    document.body.appendChild(newDivEl);

    const newVideoElement = document.createElement('VIDEO');
    newVideoElement.setAttribute('id', 'myVideo');
    newVideoElement.setAttribute("src", './countdown.mp4');
    newVideoElement.setAttribute("width", "1980"); // 동영상 가로크기
    newVideoElement.setAttribute("height", "1100"); // 동영상 세로크기
    newVideoElement.setAttribute('autoplay', 'true');
    document.getElementById('result').appendChild(newVideoElement);
    newVideoElement.scrollIntoView({ behavior: 'smooth', block: 'end' });

    const video = document.getElementById('myVideo');
    video.addEventListener('ended', videoEnded);
    function videoEnded() {
        newVideoElement.classList.add('fade-out-box');
        setTimeout(function () {
            video.remove(video);
            //newDivEl.classList.add('fade-in-box');
            newDivEl.style.backgroundImage = 'url(./img/screen.png)';
            newDivEl.style.backgroundSize = 'cover';
            newDivEl.style.width = '1920px';
            newDivEl.style.height = '955px';

            newDivEl.scrollIntoView({ behavior: 'smooth', block: 'end' });
        }, 2000);
        const resultRegEl = document.createElement('div');
        const resultRegTotalEl = document.createElement('div');
        const resultTxtEl = document.createElement('div');
        const resultTxt2El = document.createElement('div');
        document.getElementById('result').appendChild(resultRegEl);
        resultRegEl.style.visibility = 'hidden';
        setTimeout(() => {
            resultRegEl.style.visibility = 'visible ';
            resultRegEl.classList.add('fade-in-box');
        }, 3000);
        resultRegEl.style.position = 'relative';
        resultRegEl.style.top = '22%';
        resultRegEl.style.fontSize = '100px';
        resultRegEl.style.marginBottom = '0';
        resultRegEl.style.fontFamily = "'SBAggroB', sans-serif";
        resultRegEl.style.textAlign = 'center';
        resultRegEl.textContent = movie_name.value;

        document.getElementById('result').appendChild(resultTxtEl);
        resultTxtEl.style.position = 'relative';
        resultTxtEl.style.top = '24%';
        resultTxtEl.style.fontSize = '50px';
        resultTxtEl.style.marginBottom = '0';
        resultTxtEl.style.fontFamily = "'SBAggroB', sans-serif";
        resultTxtEl.style.textAlign = 'center';
        resultTxtEl.textContent = '이 영화의 관객수는';

        document.getElementById('result').appendChild(resultRegTotalEl);
        resultRegTotalEl.style.visibility = 'hidden';
        setTimeout(() => {
            resultRegTotalEl.style.visibility = 'visible ';
            resultRegTotalEl.classList.add('fade-in-box');
        }, 5000);
        resultRegTotalEl.style.position = 'relative';
        resultRegTotalEl.style.top = '27%';
        resultRegTotalEl.style.right = '10%';
        resultRegTotalEl.style.fontSize = '100px';
        resultRegTotalEl.style.fontFamily = "'SBAggroB', sans-serif";
        resultRegTotalEl.style.textAlign = 'center';
        const startNumber = 0;
        const endNumber = Math.round(output1[0] * 1000);
        const intervalTime = 10; // 밀리초 단위

        // setInterval() 함수를 사용하여 일정 간격으로 숫자를 증가시키고 표시
        let currentNumber = startNumber;
        const interval = setInterval(() => {
            // 현재 숫자가 종료 숫자보다 작으면 숫자를 랜덤하게 증가시키고 값을 텍스트에 표시
            if (currentNumber < endNumber) {
                currentNumber += Math.floor(Math.random() * 30); // 0부터 9까지 랜덤한 수를 생성하여 더함
                resultRegTotalEl.textContent = currentNumber;
            } else { // 종료 숫자에 도달하면 clearInterval() 함수를 사용하여 간격을 정지
                clearInterval(interval);
            }
        }, intervalTime);

        document.getElementById('result').appendChild(resultTxt2El);
        resultTxt2El.style.position = 'relative';
        resultTxt2El.style.top = '18.5%';
        resultTxt2El.style.left = '10%';
        resultTxt2El.style.fontSize = '50px';
        resultTxt2El.style.marginBottom = '0';
        resultTxt2El.style.fontFamily = "'SBAggroB', sans-serif";
        resultTxt2El.style.textAlign = 'center';
        resultTxt2El.textContent = '명으로 예상됩니다.';

    }
}

document.getElementById("cls_btn").onclick = () => {
    if (document.getElementById('result')) {
        document.getElementById('result').remove(document.getElementById('result'));
    }
    if (document.getElementById('result')) {
        document.getElementById('result').remove(document.getElementById('result'));
    }

    const newDivEl = document.createElement('div');
    newDivEl.setAttribute('id', 'result');
    document.body.appendChild(newDivEl);

    const newVideoElement = document.createElement('VIDEO');
    newVideoElement.setAttribute('id', 'myVideo');
    newVideoElement.setAttribute("src", './countdown.mp4');
    newVideoElement.setAttribute("width", "1980"); // 동영상 가로크기
    newVideoElement.setAttribute("height", "1100"); // 동영상 세로크기
    newVideoElement.setAttribute('autoplay', 'true');
    document.getElementById('result').appendChild(newVideoElement);
    newVideoElement.scrollIntoView({ behavior: 'smooth', block: 'end' });

    const video = document.getElementById('myVideo');
    video.addEventListener('ended', videoEnded);
    function videoEnded() {
        newVideoElement.classList.add('fade-out-box');
        setTimeout(function () {
            video.remove(video);
            //newDivEl.classList.add('fade-in-box');
            newDivEl.style.backgroundImage = 'url(./img/screen.png)';
            newDivEl.style.backgroundSize = 'cover';
            newDivEl.style.width = '1920px';
            newDivEl.style.height = '955px';

            newDivEl.scrollIntoView({ behavior: 'smooth', block: 'end' });

            const newDonut1El = document.createElement('div');
            newDonut1El.classList.add('donut-container');
            newDonut1El.setAttribute('id', 'donut-container');
            newDonut1El.style.position = 'relative';
            newDonut1El.style.top = '28%';
            newDonut1El.style.right = '10%';
            document.getElementById('result').appendChild(newDonut1El);

            const newName1El = document.createElement('div');
            document.getElementById('result').appendChild(newName1El);
            newName1El.style.position = 'relative';
            newName1El.style.top = '-45%';
            newName1El.style.fontSize = '100px';
            newName1El.style.marginBottom = '0';
            newName1El.style.fontFamily = "'SBAggroB', sans-serif";
            newName1El.style.textAlign = 'center';
            newName1El.textContent = movie_name.value;

            const newDonut2El = document.createElement('div');
            newDonut2El.classList.add('donut');
            document.getElementById('donut-container').appendChild(newDonut2El);

            const donut = document.getElementsByClassName("donut")[0]

            let totalMinwon = 0;

            let cls = 0;
            for (let i = 0; i < output2.length - 1; i++) {
                if (output2[i] < output2[i + 1]) cls = i + 1;
                else cls = i;
            }
            switch (cls) {
                case 0:
                    totalMinwon = 0;
                    break;
                case 1:
                    totalMinwon = 25;
                    break;
                case 2:
                    totalMinwon = 50;
                    break;
                case 3:
                    totalMinwon = 75;
                    break;
                case 4:
                    totalMinwon = 100;
                    break;
            }

            let t4 = 0
            const donutAnimation = setInterval(() => {
                donut.dataset.percent = t4;
                donut.style.background = `conic-gradient(#4F98FF 0 ${t4}%, #DEDEDE ${t4}% 100% )`;
                t4++ >= totalMinwon && clearInterval(donutAnimation);
            }, 50);


            const newName2El = document.createElement('div');
            document.getElementById('result').appendChild(newName2El);
            newName2El.style.position = 'relative';
            newName2El.style.top = '-18%';
            newName2El.style.left = '20%';
            newName2El.style.fontSize = '50px';
            newName2El.style.marginBottom = '0';
            newName2El.style.fontFamily = "'SBAggroB', sans-serif";
            newName2El.style.textAlign = 'center';
            switch (cls) {
                case 0:
                    newName2El.textContent = '100만명미만으로 예상';
                    break;
                case 1:
                    newName2El.textContent = '100만명이상 150만명 미만으로 예상';
                    break;
                case 2:
                    newName2El.textContent = '150만명이상 300만명 미만으로 예상';
                    break;
                case 3:
                    newName2El.textContent = '300만명이상 500만명명 미만으로 예상';
                    break;
                case 4:
                    newName2El.textContent = '500만명이상으로 예상';
                    break;
            }

        }, 2000);
    }

}

document.getElementById("all_btn").onclick = () => {
    if (document.getElementById('result')) {
        document.getElementById('result').remove(document.getElementById('result'));
    }
    if (Math.round(output1[0] * 1000) < 50000) {
        const newDivEl = document.createElement('div');
        newDivEl.setAttribute('id', 'result');
        document.body.appendChild(newDivEl);

        const newVideoElement = document.createElement('VIDEO');
        newVideoElement.setAttribute('id', 'myVideo');
        newVideoElement.setAttribute("src", './countdown.mp4');
        newVideoElement.setAttribute("width", "1980"); // 동영상 가로크기
        newVideoElement.setAttribute("height", "1100"); // 동영상 세로크기
        newVideoElement.setAttribute('autoplay', 'true');
        document.getElementById('result').appendChild(newVideoElement);
        newVideoElement.scrollIntoView({ behavior: 'smooth', block: 'end' });

        const video = document.getElementById('myVideo');
        video.addEventListener('ended', videoEnded);
        function videoEnded() {
            newVideoElement.classList.add('fade-out-box');
            setTimeout(function () {
                video.remove(video);
                //newDivEl.classList.add('fade-in-box');
                newDivEl.style.backgroundImage = 'url(./img/screen.png)';
                newDivEl.style.backgroundSize = 'cover';
                newDivEl.style.width = '1920px';
                newDivEl.style.height = '955px';

                newDivEl.scrollIntoView({ behavior: 'smooth', block: 'end' });
            }, 2000);
            const resultRegEl = document.createElement('div');
            const resultRegTotalEl = document.createElement('div');
            const resultTxtEl = document.createElement('div');
            const resultTxt2El = document.createElement('div');
            document.getElementById('result').appendChild(resultRegEl);
            resultRegEl.style.visibility = 'hidden';
            setTimeout(() => {
                resultRegEl.style.visibility = 'visible ';
                resultRegEl.classList.add('fade-in-box');
            }, 3000);
            resultRegEl.style.position = 'relative';
            resultRegEl.style.top = '22%';
            resultRegEl.style.fontSize = '100px';
            resultRegEl.style.marginBottom = '0';
            resultRegEl.style.fontFamily = "'SBAggroB', sans-serif";
            resultRegEl.style.textAlign = 'center';
            resultRegEl.textContent = movie_name.value;

            document.getElementById('result').appendChild(resultTxtEl);
            resultTxtEl.style.position = 'relative';
            resultTxtEl.style.top = '24%';
            resultTxtEl.style.fontSize = '50px';
            resultTxtEl.style.marginBottom = '0';
            resultTxtEl.style.fontFamily = "'SBAggroB', sans-serif";
            resultTxtEl.style.textAlign = 'center';
            resultTxtEl.textContent = '영화에 대한';

            document.getElementById('result').appendChild(resultRegTotalEl);
            resultRegTotalEl.style.visibility = 'hidden';
            setTimeout(() => {
                resultRegTotalEl.style.visibility = 'visible ';
                resultRegTotalEl.classList.add('fade-in-box');
            }, 5000);
            resultRegTotalEl.style.position = 'relative';
            resultRegTotalEl.style.top = '27%';
            resultRegTotalEl.style.right = '10%';
            resultRegTotalEl.style.fontSize = '100px';
            resultRegTotalEl.style.fontFamily = "'SBAggroB', sans-serif";
            resultRegTotalEl.style.textAlign = 'center';
            const startNumber = 0;
            const endNumber = Math.round(output1[0] * 1000);
            const intervalTime = 10; // 밀리초 단위

            // setInterval() 함수를 사용하여 일정 간격으로 숫자를 증가시키고 표시
            let currentNumber = startNumber;
            const interval = setInterval(() => {
                // 현재 숫자가 종료 숫자보다 작으면 숫자를 랜덤하게 증가시키고 값을 텍스트에 표시
                if (currentNumber < endNumber) {
                    currentNumber += Math.floor(Math.random() * 30); // 0부터 9까지 랜덤한 수를 생성하여 더함
                    resultRegTotalEl.textContent = currentNumber;
                } else { // 종료 숫자에 도달하면 clearInterval() 함수를 사용하여 간격을 정지
                    clearInterval(interval);
                }
            }, intervalTime);

            document.getElementById('result').appendChild(resultTxt2El);
            resultTxt2El.style.position = 'relative';
            resultTxt2El.style.top = '18.5%';
            resultTxt2El.style.left = '10%';
            resultTxt2El.style.fontSize = '50px';
            resultTxt2El.style.marginBottom = '0';
            resultTxt2El.style.fontFamily = "'SBAggroB', sans-serif";
            resultTxt2El.style.textAlign = 'center';
            resultTxt2El.textContent = '명으로 예상됩니다.';

        }
    }
    else {
        if (document.getElementById('result')) {
            document.getElementById('result').remove(document.getElementById('result'));
        }
        if (document.getElementById('result')) {
            document.getElementById('result').remove(document.getElementById('result'));
        }

        const newDivEl = document.createElement('div');
        newDivEl.setAttribute('id', 'result');
        document.body.appendChild(newDivEl);

        const newVideoElement = document.createElement('VIDEO');
        newVideoElement.setAttribute('id', 'myVideo');
        newVideoElement.setAttribute("src", './countdown.mp4');
        newVideoElement.setAttribute("width", "1980"); // 동영상 가로크기
        newVideoElement.setAttribute("height", "1100"); // 동영상 세로크기
        newVideoElement.setAttribute('autoplay', 'true');
        document.getElementById('result').appendChild(newVideoElement);
        newVideoElement.scrollIntoView({ behavior: 'smooth', block: 'end' });

        const video = document.getElementById('myVideo');
        video.addEventListener('ended', videoEnded);
        function videoEnded() {
            newVideoElement.classList.add('fade-out-box');
            setTimeout(function () {
                video.remove(video);
                //newDivEl.classList.add('fade-in-box');
                newDivEl.style.backgroundImage = 'url(./img/screen.png)';
                newDivEl.style.backgroundSize = 'cover';
                newDivEl.style.width = '1920px';
                newDivEl.style.height = '955px';

                newDivEl.scrollIntoView({ behavior: 'smooth', block: 'end' });

                const newDonut1El = document.createElement('div');
                newDonut1El.classList.add('donut-container');
                newDonut1El.setAttribute('id', 'donut-container');
                newDonut1El.style.position = 'relative';
                newDonut1El.style.top = '28%';
                newDonut1El.style.right = '10%';
                document.getElementById('result').appendChild(newDonut1El);

                const newName1El = document.createElement('div');
                document.getElementById('result').appendChild(newName1El);
                newName1El.style.position = 'relative';
                newName1El.style.top = '-45%';
                newName1El.style.fontSize = '100px';
                newName1El.style.marginBottom = '0';
                newName1El.style.fontFamily = "'SBAggroB', sans-serif";
                newName1El.style.textAlign = 'center';
                newName1El.textContent = movie_name.value;

                const newDonut2El = document.createElement('div');
                newDonut2El.classList.add('donut');
                document.getElementById('donut-container').appendChild(newDonut2El);

                const donut = document.getElementsByClassName("donut")[0]

                let totalMinwon = 0;

                let cls = 0;
                for (let i = 0; i < output2.length - 1; i++) {
                    if (output2[i] < output2[i + 1]) cls = i + 1;
                    else cls = i;
                }
                switch (cls) {
                    case 0:
                        totalMinwon = 0;
                        break;
                    case 1:
                        totalMinwon = 25;
                        break;
                    case 2:
                        totalMinwon = 50;
                        break;
                    case 3:
                        totalMinwon = 75;
                        break;
                    case 4:
                        totalMinwon = 100;
                        break;
                }

                let t4 = 0
                const donutAnimation = setInterval(() => {
                    donut.dataset.percent = t4;
                    donut.style.background = `conic-gradient(#4F98FF 0 ${t4}%, #DEDEDE ${t4}% 100% )`;
                    t4++ >= totalMinwon && clearInterval(donutAnimation);
                }, 50);


                const newName2El = document.createElement('div');
                document.getElementById('result').appendChild(newName2El);
                newName2El.style.position = 'relative';
                newName2El.style.top = '-18%';
                newName2El.style.left = '20%';
                newName2El.style.fontSize = '50px';
                newName2El.style.marginBottom = '0';
                newName2El.style.fontFamily = "'SBAggroB', sans-serif";
                newName2El.style.textAlign = 'center';
                switch (cls) {
                    case 0:
                        newName2El.textContent = '100만명미만으로 예상';
                        break;
                    case 1:
                        newName2El.textContent = '100만명이상 150만명 미만으로 예상';
                        break;
                    case 2:
                        newName2El.textContent = '150만명이상 300만명 미만으로 예상';
                        break;
                    case 3:
                        newName2El.textContent = '300만명이상 500만명 미만으로 예상';
                        break;
                    case 4:
                        newName2El.textContent = '500만명이상으로 예상';
                        break;
                }

            }, 2000);
        }
    }
}