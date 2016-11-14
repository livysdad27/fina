function tableCellGet(myClass, x, y){
  var jqstr = myClass + ' tbody tr:nth-child(' + y + ') td:nth-child(' + x + ')';
  return $(jqstr).html()
}

function tableCellSet(myClass, x, y, myVal){
  var jqstr = myClass + ' tbody tr:nth-child(' + y + ') td:nth-child(' + x + ')';
  $(jqstr).html(myVal);
}

function makeTid(myClass){
  for(i = 1; i <= $(myClass + ' tbody tr').length; i++){
    var id = tableCellGet(myClass, 2, i);
    var tid = "<a href='api/trans?tid=" + encodeURIComponent(id) + "'>" + id + "</a>";
    tableCellSet(myClass, 2, i, tid);
  };
}

function makeCatLink(myClass){
  for(i = 1; i <= $(myClass + ' tbody tr').length; i++){
    var cat = tableCellGet(myClass, 5, i);
    var tid = "<a href='api/trans?cat=" + encodeURIComponent(cat) + "'>" + cat + "</a>";
    tableCellSet(myClass, 5, i, tid);
  };
}

function catAreaUpdate(){
  $.ajax({
    'url' : 'api/trans',
    'type' : 'GET',
    'data' : { cat: ''},
    'success' : function(data){
      if(data == ''){
        $('.catInput').hide();
      } 
      $('.catArea').html(data);
    }
  });
}

var transLength = 0
function transAreaUpdate(){
  $.ajax({
    'url' : 'api/trans',
    'type'  :  'GET',
    'success' : function(data){
        $('.transArea').html(data);
        makeTid(".transTable");
        makeCatLink(".transTable");
     
    }  
  });
}

function graphUpdate(gType, sDate, eDate){
  var now = new Date().getTime();
  if ((typeof(eDate) == 'undefined') || (typeof(sDate) == 'undefined')){
    $('.graphImage').attr('src', '/api/trans?graph=' + gType + "&now=" + now);
  }
  else{
    $('.graphImage').attr('src', '/api/trans?graph=' + encodeURI( gType + '&startDate=' + sDate + '&endDate=' + eDate + "&now=" + now));
  }
}

function updateAll(){
  catAreaUpdate();
  transAreaUpdate();
  graphUpdate('pareto');
}
  

$(document).ready(function(){

  Dropzone.options.ofxFileDropzone = {
    paramName:  "tFile",
    maxFilesize:  2,
    method:  "put",
    accept:  function(file, done) {
               done();
             },
    complete:  function(){
             updateAll();
           }
  };

  updateAll();

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
          graphUpdate('pareto', $('input[name=startDate]').val(), $('input[name=endDate]').val());
      }  
    });
  });

  $('input[name=newCat]').keypress(function(e) {
    if(e.which == 13){
      $.ajax({
        'url' : 'api/trans',
        'type' : 'POST',
        'data' : {
                   cat:  $('input[name=newCat]').val(),
                   payee: tableCellGet('.payeeTable', 2, 1)
                 },
        'success' : function(data){
          updateAll();
        }
      });
      $('input[name=newCat]').val('');
    }
  });
});
