$(document).ready(function(){

  var now = new Date();

  var nowStr = now.getFullYear() + '-' 
             + ('00' + (now.getMonth() + 1)).slice(-2) + '-' 
             + ('00' + now.getDate()).slice(-2) + 'T' 
             + ('00' + now.getHours()).slice(-2) + ':'
             + ('00' + now.getMinutes()).slice(-2); 
//  $('input[name=startDate]').val("2016-01-01T00:00:00");
//  $('input[name=endDate]').val(nowStr);

  $('button[name=queryButton]').click(function() {
    $.ajax({
      'url' : 'api/trans',
      'type'  :  'GET',
      'data' :  {
                  startDate:  $('input[name=startDate]').val(),
                  endDate:  $('input[name=endDate]').val()
                 },
      'success' : function(data){
          $('.transArea').html(data);
      }  
    });
  });
});
