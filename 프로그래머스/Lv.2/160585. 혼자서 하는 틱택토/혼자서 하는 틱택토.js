// 불가능 조건 [1] : cntO < cntX
// 불가능 조건 [2] : cntO > cntX + 1
// 불가능 조건 [3] : winO && winX <- 판별할 때 cntO랑 xntX 수가 둘다 3 이상이면
// 불가능 조건 [4] : winX만 true인데 cntO가 cntX보다 많을 때
// 불가능 조건 [5] : winO만 true인데 cntO과 cntX가 같을 때

function solution(board) {
    // O 개수랑 X 개수 세기
    let ans;
    let cntO = 0;
    let cntX = 0;
    let winO = false;
    let winX = false;
    for (let r = 0; r < 3; r++) {
        for (let c = 0; c < 3; c++) {
            if (board[r][c] === 'O') {
                cntO++;
            } else if (board[r][c] === 'X') {
                cntX++;
            }
        }
    }
    
    if (cntO < cntX || cntO > cntX + 1) {
        return 0
    }
    
    
    for (let x = 0; x < 3; x++) {
        let widthStateO = 0;
        let widthStateX = 0;
        let heightStateO = 0;
        let heightStateX = 0;

        for (let y = 0; y < 3; y++) {
            if (board[x][y] === 'O') {  // 가로
                widthStateO++;
            } else if (board[x][y] === 'X') {
                widthStateX++;
            }

            if (board[y][x] === 'O') {  // 세로
                heightStateO++;
            } else if (board[y][x] === 'X') {
                heightStateX++;
            }
        }
        if (widthStateO === 3 || heightStateO === 3) {
            winO = true;
        } else if (widthStateX === 3 || heightStateX === 3) {
            winX = true;
        }
    }

    // 대각선 판별 - 우하향
    if (board[0][0] === board[1][1] && board[1][1] === board[2][2]) {
        if (board[1][1] === 'O') {
            winO = true;
        } else if (board[1][1] === 'X') {
            winX = true;
        }
    }

    // 대각선 판별 - 우상향
    if (board[2][0] === board[1][1] && board[1][1] === board[0][2]) {
        if (board[1][1] === 'O') {
            winO = true;
        } else if (board[1][1] === 'X') {
            winX = true;
        }
    }

    if (winO === true && winX === true) {
        return 0
    }

    
    if (cntO > cntX && winO === false && winX === true) {
        return 0
    }
    
    if (cntO === cntX && winO === true && winX === false) {
        return 0
    }
    
    return 1
}