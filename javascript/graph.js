const depthFirstPrint = (graph, source) => {
    const stack = [ source ];

    while(stack.length > 0){
        const current = stack.pop(); //remove end of array
        console.log(current);
        for (let neighbor of graph[current]) {
            stack.push(neighbor); //add to end of list
        }
    }
};

const graph = {
    a: ['b', 'c'],
    b: ['d'],
    c: ['e'],
    d: ['f'],
    e: [],
    f: []
};

depthFirstPrint(graph, 'a');
