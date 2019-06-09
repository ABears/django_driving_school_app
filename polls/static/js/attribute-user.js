$('.btn-attribute-user').click(function(){

    let studentId = $(this).attr('data-button');
    let instuctorId =  $('.s-' + studentId).val();
    let attributeStudentUrl = 'attribute-student/' + instuctorId + '/' + studentId
    let token = $('.get-csrf-token').children().val()
    let data = {csrfmiddlewaretoken: token };
    $.ajax({
        type: "POST",
        url: attributeStudentUrl,
        data: data,
        success: function(response) {
            console.log(response);
            window.location.reload();
        }
    })
})