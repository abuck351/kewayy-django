$(document).on('show.bs.modal', '#confirmDeleteModal', function (event) {
    let button = $(event.relatedTarget); // The button that triggered the modal
    let testCaseHref = button.data('testcasehref');
    let testCaseCriteria = button.data('testcasecriteria');

    let modal = $(this);
    modal.find('#deleteButton').attr('href', testCaseHref);
    modal.find('#deleteCriteria').text(testCaseCriteria);
})