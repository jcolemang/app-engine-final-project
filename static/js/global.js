
// initialize
(function () {
    Rx.Observable.of([1, 2, 3, 4, 5])
        .map(num => 2 * num)
        .subscribe(num => {
            console.log(num);
        });
})();
