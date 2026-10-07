export function employeesPage() {
  return `
    <div class="d-flex justify-content-between align-items-center mb-4">
      <div>
        <h1>Сотрудники</h1>
        <p class="text-muted mb-0">Управление сотрудниками организации</p>
      </div>
      <button type="button" class="btn btn-primary" onclick="route('employeeCreate')">
        + Добавить сотрудника
      </button>
    </div>
    <div class="card shadow-sm mb-4">
      <div class="card-body">
        <div class="row g-3">
          <div class="col-md-6">
            <input type="text" class="form-control" placeholder="Поиск по ФИО" />
          </div>
          <div class="col-md-4">
            <select class="form-select">
              <option selected>Все подразделения</option>
              <option>IT-отдел</option>
              <option>Бухгалтерия</option>
              <option>Отдел кадров</option>
            </select>
          </div>
          <div class="col-md-2">
            <button class="btn btn-primary w-100">Найти</button>
          </div>
        </div>
      </div>
    </div>
    <div class="card shadow-sm">
      <div class="card-body">
        <div class="table-responsive">
          <table class="table table-hover align-middle">
            <thead>
              <tr>
                <th>ФИО</th>
                <th>Должность</th>
                <th>Подразделение</th>
                <th>Телефон</th>
                <th>Имущества на руках</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Иванов Иван Иванович</td>
                <td>Программист</td>
                <td>IT-отдел</td>
                <td>+7 900 000-00-01</td>
                <td>4</td>
                <td>
                  <button class="btn btn-sm btn-outline-primary" data-bs-toggle="modal" data-bs-target="#employeeModal">
                    Открыть
                  </button>
                </td>
              </tr>
              <tr>
                <td>Петров Пётр Петрович</td>
                <td>Бухгалтер</td>
                <td>Бухгалтерия</td>
                <td>+7 900 000-00-02</td>
                <td>2</td>
                <td>
                  <button class="btn btn-sm btn-outline-primary">Открыть</button>
                </td>
              </tr>
              <tr>
                <td>Сидоров Алексей Сергеевич</td>
                <td>Системный администратор</td>
                <td>IT-отдел</td>
                <td>+7 900 000-00-03</td>
                <td>6</td>
                <td>
                  <button class="btn btn-sm btn-outline-primary">Открыть</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    <div class="modal fade" id="employeeModal" tabindex="-1">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Иванов Иван Иванович</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
          </div>
          <div class="modal-body">
            <p><strong>Должность:</strong> Программист</p>
            <p><strong>Подразделение:</strong> IT-отдел</p>
            <p><strong>Email:</strong> ivanov@example.com</p>
            <h6 class="mt-4">Имущество на руках</h6>
            <table class="table">
              <thead>
                <tr>
                  <th>Инв. номер</th>
                  <th>Название</th>
                  <th>Дата выдачи</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>INV-0002</td>
                  <td>Dell UltraSharp</td>
                  <td>10.06.2025</td>
                </tr>
                <tr>
                  <td>INV-0005</td>
                  <td>Ноутбук HP</td>
                  <td>12.06.2025</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Закрыть</button>
          </div>
        </div>
      </div>
    </div>
  `
}

export function employeeCreatePage() {
  return `
    <div class="mb-4">
      <button type="button" class="btn btn-link text-decoration-none p-0" onclick="route('employees')">
        ← Назад к сотрудникам
      </button>
      <h1 class="mt-3">Добавление сотрудника</h1>
      <p class="text-muted">Добавление нового сотрудника в систему</p>
    </div>
    <div class="row g-4">
      <div class="col-md-8">
        <div class="card shadow-sm">
          <div class="card-header">Основная информация</div>
          <div class="card-body">
            <form onsubmit="event.preventDefault(); route('employees')">
              <div class="mb-3">
                <label for="fullName" class="form-label"> ФИО </label>
                <input type="text" class="form-control" id="fullName" placeholder="Например, Иванов Иван Иванович" required />
              </div>
              <div class="mb-3">
                <label for="position" class="form-label"> Должность </label>
                <input type="text" class="form-control" id="position" placeholder="Например, Программист" required />
              </div>
              <div class="mb-3">
                <label for="department" class="form-label"> Подразделение </label>
                <select class="form-select" id="department" required>
                  <option value="" selected disabled>Выберите подразделение</option>
                  <option value="it">IT-отдел</option>
                  <option value="accounting">Бухгалтерия</option>
                  <option value="hr">Отдел кадров</option>
                </select>
              </div>
              <div class="mb-3">
                <label for="phone" class="form-label"> Телефон </label>
                <input type="tel" class="form-control" id="phone" placeholder="+7 900 000-00-00" required />
              </div>
              <div class="mb-4">
                <label for="email" class="form-label"> Email </label>
                <input type="email" class="form-control" id="email" placeholder="employee@example.com" required />
              </div>
              <div class="d-flex gap-2">
                <button type="submit" class="btn btn-primary">Добавить сотрудника</button>
                <button type="button" class="btn btn-outline-secondary" onclick="route('employees')">Отмена</button>
              </div>
            </form>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card shadow-sm">
          <div class="card-header">После добавления</div>
          <div class="card-body">
            <p class="mb-3">Новый сотрудник будет добавлен в список сотрудников организации.</p>
            <div class="mb-3">
              <div class="text-muted mb-1">Имущество на руках</div>
              <div>0</div>
            </div>
            <div>
              <div class="text-muted mb-1">Ответственный</div>
              <div>Сотрудник будет доступен для оформления выдачи имущества.</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  `
}
