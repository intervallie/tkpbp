$(document).ready(function() {
    $(document).on("click",".btn-delete",function(){
        var this_html=$(this);
        this_html.attr("disabled","disabled");
        this_html.text("DELETING....");
        var id=this_html.parent().parent().children().first().text();
        console.log(id)
        //console.log(id);
        $.ajax({
            url:"../artikel/delete_post",
            type:'POST',
            data:{
                title: id},
        })
        .done(function(response){
            if(response['error']==false){
                this_html.parent().parent().remove();
                $("#upt_error").hide();
                $("#upt_success").text(response['errorMessage']);
                $("#upt_success").show();

            }
            else{
                $("#upt_success").hide();
                $("#upt_error").text(response['errorMessage']);
                $("#upt_error").show();
                console.log("else")
            }
            console.log(response);
        })
        .fail(function(){
             $("#upt_success").hide();
             $("#upt_error").text("Something Went Wrong!");
             $("#upt_error").show();
        });
    });
    
});


