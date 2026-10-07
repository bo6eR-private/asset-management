export function reportsPage() {
  return `
    <div class="mb-4">
      <h1>Отчёты</h1>
      <p class="text-muted">Формирование отчётов по материальным ценностям</p>
    </div>
    <div class="card shadow-sm mb-4">
      <div class="card-header">Параметры отчёта</div>
      <div class="card-body">
        <div class="row g-3">
          <div class="col-md-4">
            <label class="form-label"> Тип отчёта </label>
            <select class="form-select">
              <option selected>Выберите тип отчёта</option>
              <option>Отчёт по имуществу</option>
              <option>Отчёт по сотрудникам</option>
              <option>Отчёт по выдачам</option>
              <option>Отчёт по возвратам</option>
            </select>
          </div>
          <div class="col-md-3">
            <label class="form-label"> С даты </label>
            <input type="date" class="form-control" />
          </div>
          <div class="col-md-3">
            <label class="form-label"> По дату </label>
            <input type="date" class="form-control" />
          </div>
          <div class="col-md-2 d-flex align-items-end">
            <button class="btn btn-primary w-100">Сформировать</button>
          </div>
        </div>
      </div>
    </div>
    <h4 class="mb-3">Доступные отчёты</h4>
    <div class="row g-4">
      <div class="col-md-6">
        <div class="card shadow-sm h-100">
          <div class="card-body">
            <h5>Отчёт по имуществу</h5>
            <p class="text-muted">
              Список материальных ценностей с указанием состояния и текущего статуса.
            </p>
            <button class="btn btn-outline-primary">Сформировать</button>
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="card shadow-sm h-100">
          <div class="card-body">
            <h5>Отчёт по сотрудникам</h5>
            <p class="text-muted">Сотрудники и закреплённые за ними материальные ценности.</p>
            <button class="btn btn-outline-primary">Сформировать</button>
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="card shadow-sm h-100">
          <div class="card-body">
            <h5>Отчёт по выдачам</h5>
            <p class="text-muted">История выдачи материальных ценностей сотрудникам.</p>
            <button class="btn btn-outline-primary">Сформировать</button>
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="card shadow-sm h-100">
          <div class="card-body">
            <h5>Отчёт по возвратам</h5>
            <p class="text-muted">История возврата имущества и его состояние после возврата.</p>
            <button class="btn btn-outline-primary">Сформировать</button>
          </div>
        </div>
      </div>
    </div>
    <div class="card shadow-sm mt-4">
      <div class="card-body">
        <h5>Экспорт</h5>
        <p class="text-muted">После формирования отчёта его можно сохранить в выбранном формате.</p>
        <button class="btn btn-outline-danger me-2">Экспорт в PDF</button>
        <button class="btn btn-outline-success">Экспорт в Excel</button>
      </div>
    </div>
  `
}
