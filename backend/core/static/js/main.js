(function() {
  // Chama o método pra numerar os objetos ao carregar a página.
  reorderItems()
})();

document.querySelector('#addItem').addEventListener('click', function() {
  setTimeout(() => {
    reorderItems()
  }, 500)
})

function reorderItems() {
  Array.from(document.querySelectorAll("[id^='item-']"))
    .forEach((item, i) => {
      item.setAttribute('id', 'item-' + i)

      if (!item.querySelector('[data-field="order"]')) {
        return
      }

      item.querySelector('[data-field="order"]').setAttribute('name', 'items-' + i + '-order')
      item.querySelector('[data-field="order"]').setAttribute('id', 'id_items-' + i + '-order')

  })

  Array.from(document.querySelectorAll("#id_id"))
    .forEach((item, i) => item.setAttribute('name', 'items-' + (i + 1) + '-id'))

  let totalItems = $('#order').children().length
  document.querySelector('#id_items-TOTAL_FORMS').value = totalItems

  // htmx.org/api/#process
  htmx.process(document.querySelector("#order"))
}

function removeRow() {
  const span = event.target.parentNode
  const div = span.parentNode
  div.parentNode.removeChild(div)

  reorderItems()
}

Array.from(document.querySelectorAll('.remove-row'))
  .forEach((item, i) => {
    item.addEventListener('click', function() {
      document.querySelector('button[type="submit"]').style.display = 'none'
      document.querySelector('#btn-close').style.display = 'block'
    })
  })
