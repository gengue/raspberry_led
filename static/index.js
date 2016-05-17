var elem = document.querySelector('#switch');
var init = new Switchery(elem);

elem.onchange = function(){
  console.log(elem.checked);
  toggleLed(elem.checked);
};

function toggleLed(action){
  $.ajax({
    url: '/toggle_led',
    type: 'POST',
    data: { action: action },
    success: function (data, textStatus, jqXHR) {
      console.log(data);
      $('.registry-list').append('<li><span>IP: </span>'+data.ip+
                                 ' . <span>Fecha: </span>'+data.datetime+'</li>');
    },
    error: function (jqXHR, textStatus, errorThrown) {
      alert('Ha ocurrido un error');
    }
  });
}
