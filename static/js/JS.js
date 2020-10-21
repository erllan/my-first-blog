

function ajax(){

$("button.like").click( function(event) {
event.preventDefault();
var a = $(this)
var likeCount = $(a).closest('div').find($('a.like-count'))
console.log(likeCount)
var url = a.attr('data-url')
    $.get(`${url}`,
    function(res){
    if(res.result === 'unlike'){
    a.css('background',"grey")
    likeCount.html(Number(likeCount.html()) -1)
    }else if(res.result === 'like'){
    a.css('background',"red")
    likeCount.html(Number(likeCount.html()) +1)
    }
});
})
}

function comment(){
$('#comment-form').on('submit',function(event){
event.preventDefault();
var data = $(this).serialize()
 $.post($(this).attr('action'),data,function(response){
    var h3 = $('<h3>')
    h3.html(response.user)
    var div = $("<div class = 'comments'></div>")
    div.append(h3).append(response.comment)
    $('#mycomment').prepend(div)
    })
})

}

function message(){
    var block = document.getElementById("messages");
    block.scrollTop = block.scrollHeight;

    $('#message-form').on('submit',function(event){
    event.preventDefault();
    var data = $(this).serialize()
    $.post($(this).attr('action'),data,function(response){
         var container = $('<div class="message">').css({'margin-bottom':'12px','background-color': '#red','border-radius':'7px'})
         var h3 = $('<h3 style="color:red">').html(response.user)
         container.append(h3).append(response.message)
         $('#messages').append(container)
         var block = document.getElementById("messages");
         block.scrollTop = block.scrollHeight;
         $('input#message').val('')
        })
    })
}


var accountToggle = function(){
$('.account > img').click(function(){
$('#dropdown').toggle()
})
}

function subscribe(){
$('#subscribe').on('click',function(event){
    event.preventDefault();
    var url = $(this).attr('href');
    var count = $('#subskrbs');
    $.get(`${url}`,function(resp){

    if(resp.result == 'yes'){
        $('#subscribe').html('<h3>отписаться</h3>').css('background-color','red')
        $('#subscribe h3').css('color','white')
        count.html(Number(count.html()) +1)
    }
    else if(resp.result == 'no'){
    $('#subscribe').html('<h3>подписаться</h3>').css('background-color','white')
        count.html(Number(count.html()) - 1)
    };

    });
});
}
//var count = 0;
//var Testlist = list();
//var line = readline();
//while(count < 100){
//	namb = readline()
//	testList.push(namb)
//	count ++
//};
//var MaxNamb = Math.max.apply(null, Testlist)
//var indexMaxNumb = Testlist.indexOf(MaxNamb)+1
//console.log(MaxNamb)
//console.log(indexMaxNumb)
