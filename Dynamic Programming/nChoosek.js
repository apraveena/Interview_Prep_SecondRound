function subsetsCount(n, k){

    //Base case
    if(k==0 || k==n) return 1;

    var twodarray = Array.from(Array(n+1),()=> new Array(k+1));

    console.log(twodarray)
    for (let row=0; row<n; row++ )
    {
        twodarray[row][0] = 1;
    }
    for (let col=0; col<k; col++ )
    {
        twodarray[col][col] = 1;
    }
    for (let row=2; row<n+1; row++ )
    {
        let kval = Math.min(row,k);
        for (let col=1; col<kval; col++ )
        {
            twodarray[row][col] = twodarray[row-1][col] + twodarray[row-1][col-1];
            //console.log(  twodarray[row][col]);
        }
    }
    return twodarray[n][k];

}

console.log(subsetsCount(5,3));