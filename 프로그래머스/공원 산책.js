function solution(park, routes) {
    const parkH = park.length;
    const parkW = park[0].length;
    let pointH, pointW;

    for (const i in park) {
        if (park[i].includes("S")) {
            for (const j in park[i]) {
                if (park[i][j] === "S") {
                    pointH = parseInt(i);
                    pointW = parseInt(j);
                    break;
                }
            }
        }
    }
    for (const r of routes) {
        let [d, n] = r.split(" ");
        n = parseInt(n);
        // 중복된 코드 줄이기 해야함
        switch (d) {
            case "N":
                if (pointH - n < 0) continue;
                for (let i = 1; i <= n; i++) {
                    if (park[pointH - 1][pointW] === "X") {
                        pointH = pointH + i - 1;
                        break;
                    }
                    pointH = pointH - 1;
                }
                break;
            case "S":
                if (pointH + n >= parkH) continue;
                for (let i = 1; i <= n; i++) {
                    if (park[pointH + 1][pointW] === "X") {
                        pointH = pointH - i + 1;
                        break;
                    }
                    pointH = pointH + 1;
                }
                break;
            case "W":
                if (pointW - n < 0) continue;
                for (let i = 1; i <= n; i++) {
                    if (park[pointH][pointW - 1] === "X") {
                        pointW = pointW + i - 1;
                        break;
                    }
                    pointW = pointW - 1;
                }
                break;
            case "E":
                if (pointW + n >= parkW) continue;
                for (let i = 1; i <= n; i++) {
                    if (park[pointH][pointW + 1] === "X") {
                        pointW = pointW - i + 1;
                        break;
                    }
                    pointW = pointW + 1;
                }
                break;
        }
    }
    return [pointH, pointW];
}
