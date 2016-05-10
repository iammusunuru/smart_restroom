$(document).ready(function(){

    var url="http://localhost:3000";
    var refreshId;
    function getInitialValues(){
        console.log($("#roomSelect").val());
        $.ajax({
            url: url+"/initialData/"+$("#roomSelect").val(),
            type:"GET",
            success: successFunction,
            error:errorFunction
        });
    };

    getInitialValues();

    function successFunction(data){
        window.clearInterval(refreshId);
            var data ={
                "temperature" : 71,
                "humidity": 34,
                "vacancy" : 2,
                "persons": 3
            };
        $("#tempIndex").html(Math.floor((Math.random() * 10) + 1));
        $('#humidity').html(Math.floor((Math.random() * 10) + 1));
        $("#vacancy").html(Math.floor((Math.random() * 10) + 1));
        $("#persons").html(Math.floor((Math.random() * 10) + 1));
         refreshId = setInterval(getData,10000);
    }

    function getData() {
            getInitialValues();
    }

    function errorFunction(data){
            console.log(data);
    }

    $( "#roomSelect" ).change(function() {
        getInitialValues();
    });

});



