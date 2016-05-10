$(document).ready(function(){

    var url="http://localhost:8000";
    var refreshId;
    function getInitialValues(){
        $.ajax({
            url: url+"/loaddata/?restroom_id="+$("#roomSelect").val(),
            type:"GET",
            success: successFunction,
            error:errorFunction
        });
    };

    getInitialValues();

    function successFunction(data){
        window.clearInterval(refreshId);
        var vacStatus =0;
        if(data === ""){
            $("#tempIndex").html("N");
            $("#humIndex").html("A");
            $('#humidity').html("N/A");
            $("#vacancy").html("N/A");
            $("#roomNum").html("N/A");
            $("#persons").html("N/A");
            refreshId = setInterval(getData,10000);
        }else{
            var resp = JSON.parse(data);
            console.log(resp);
            console.log(resp["door"]);
            console.log(resp.door.length);
            for(var i=0;i<resp.door.length;i++){
                if(resp.door[i].status === 0){
                    vacStatus++;
                }
            }
            $("#tempIndex").html(resp.temp);
            $("#humIndex").html(resp.humidity);
            if(resp.service == 1){
                $('#humidity').html("Service Needed");
            }else{
                $('#humidity').html("OK");
            }

            $("#vacancy").html(vacStatus);
            $("#roomNum").html(resp.door.length);
            $("#persons").html(resp.person_rate);
            refreshId = setInterval(getData,10000);
        }

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



