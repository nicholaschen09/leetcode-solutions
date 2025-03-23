/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let val = init; //set the value of init equal to val 
    return {
        reset() {
            val = init; //reset function
            return val;
        },
        decrement() { //decrement first then return the value
            val--;
            return val;
        },
        increment() { //increment first then return the value
            val++;
            return val;
        }

    };
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */