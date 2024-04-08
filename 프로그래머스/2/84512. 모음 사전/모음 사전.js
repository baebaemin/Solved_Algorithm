
function solution(word) {
    const alphabet = ['A', 'E', 'I', 'O', 'U'];
    const words = [];

    function dfs(currentWord) {
        words.push(currentWord);
        if (currentWord.length === 5) return;
        
        for (let i = 0; i < 5; i++) {
            dfs(currentWord + alphabet[i]);
        }
    }
    
    dfs("");  
    return words.indexOf(word);
}