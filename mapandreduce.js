var one = () => {
    var arr = [1,9,16,100]
    var res = arr.map(item => Math.sqrt(item))
    return res
}
console.log(one())

var two = () => {
    var arr =  ["Intro", "Requirements", "Analysis", "Implementation", "Conclusion", "Discussion",
        "References"]
    var res = arr.map(item => "<h1>" + item + "</h1>")
    return res
}
console.log(two())

var three = () => {
    var arr = ["i'm", "yelling", "today"]
    var res = arr.map(item => item.toUpperCase())
    return res
}
console.log(three())

var four = () => {
    var arr = ["I", "have", "looooooong", "words"]
    var res = arr.map(item => item.length)
    return res
}
console.log(four())

function reAdd(total, num) {
    return total + num;
}

var six = () => {
    var arr = [1,2,3,4,5]
    var res = arr.reduce(reAdd)
    return res
}
console.log(six())



var initialValue = 0
var seven = [{x: 1}, {x: 2}, {x: 3}].reduce(function (accumulator, currentValue) {
return accumulator + currentValue.x }, initialValue)
console.log(seven)



var eight = () => {
    var array = [[1,2], [3,4], [5,6]]
    return array.reduce(( accumulator, currentValue ) => accumulator.concat(currentValue),
  [])

}
console.log(eight())


