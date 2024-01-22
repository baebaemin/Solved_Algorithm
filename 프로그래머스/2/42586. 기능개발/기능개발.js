// while (progresses[0] !== 100) 하루가 지날때마다 각 progresses의 idx에 해당하는 speeds씩 더하기
//

function solution(progresses, speeds) {
  let answer = [];

  while (progresses.length > 0) {
    // progresses의 원소들에 개발 진행 속도만큼 더하기
    while (progresses[0] < 100) {
      for (let i = 0; i < progresses.length; i++) {
        progresses[i] += speeds[i];
      }
    }

    // while 빠져나왔을 때 = 배포 가능할 때
    let cnt = 0;
    while (progresses[0] >= 100) {
        cnt++;
        progresses.shift();
        speeds.shift();
    }
    if (cnt > 0) {
        answer.push(cnt)
    }
  }
    return answer
}
