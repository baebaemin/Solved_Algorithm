// 이동한 좌표 (시작점, 끝점) 을 set에 저장해서 길이 출력하기
const dir = {
        U: [0, -1], 
        D: [0, 1], 
        R: [1, 0], 
        L: [-1, 0]
    };

function solution(dirs) {
    const path = new Set();
    let r = 0, c = 0;
    
    for (let i = 0; i < dirs.length; i++) {
        const [dr, dc] = dir[dirs[i]];
        const nr = r + dr;
        const nc = c + dc;
        
        // 범위를 벗어나지 않았을 때
        if (-5 <= nr && nr <= 5 && -5 <= nc && nc <= 5) {
            path.add(`${r}-${c}-${nr}-${nc}`);
            path.add(`${nr}-${nc}-${r}-${c}`);
            r = nr;
            c = nc;
        }
    }
    return path.size / 2;
}