export function assetsPage() {
  return `
    <div class="d-flex justify-content-between align-items-center mb-4">
      <div>
        <h1>Материальные ценности</h1>
        <p class="text-muted">Управление имуществом</p>
      </div>
      <button type="button" class="btn btn-primary" onclick="route('assetCreate')">
        + Добавить имущество
      </button>
    </div>
    <div class="card mb-4">
      <div class="card-body">
        <div class="row g-3">
          <div class="col-md-5">
            <input type="text" class="form-control" placeholder="Поиск по названию или инвентарному номеру" />
          </div>
          <div class="col-md-3">
            <select class="form-select">
              <option selected>Все категории</option>
              <option>Компьютерная техника</option>
              <option>Мебель</option>
              <option>Оборудование</option>
            </select>
          </div>
          <div class="col-md-3">
            <select class="form-select">
              <option selected>Все статусы</option>
              <option>На складе</option>
              <option>Выдано</option>
              <option>На ремонте</option>
              <option>Списано</option>
            </select>
          </div>
          <div class="col-md-1">
            <button class="btn btn-primary w-100">Найти</button>
          </div>
        </div>
      </div>
    </div>
    <div class="card">
      <div class="card-body">
        <table class="table table-hover align-middle">
          <thead>
            <tr>
              <th>Инв. номер</th>
              <th>Название</th>
              <th>Категория</th>
              <th>Состояние</th>
              <th>Статус</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>INV-0001</td>
              <td>Lenovo ThinkPad T14</td>
              <td>Компьютерная техника</td>
              <td>Исправно</td>
              <td><span class="badge text-bg-success"> На складе </span></td>
              <td>
                <button type="button" class="btn btn-sm btn-outline-primary" onclick="route('asset')">
                  Открыть
                </button>
              </td>
            </tr>
            <tr>
              <td>INV-0002</td>
              <td>Dell UltraSharp</td>
              <td>Компьютерная техника</td>
              <td>Исправно</td>
              <td><span class="badge text-bg-primary"> Выдано </span></td>
              <td>
                <button type="button" class="btn btn-sm btn-outline-primary" onclick="route('asset')">
                  Открыть
                </button>
              </td>
            </tr>
            <tr>
              <td>INV-0003</td>
              <td>Офисное кресло</td>
              <td>Мебель</td>
              <td>Требует ремонта</td>
              <td><span class="badge text-bg-warning"> На ремонте </span></td>
              <td>
                <button type="button" class="btn btn-sm btn-outline-primary" onclick="route('asset')">
                  Открыть
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  `
}

export function assetPage() {
  return `
    <div class="mb-4">
      <button type="button" class="btn btn-link text-decoration-none p-0" onclick="route('assets')">
        ← Назад к имуществу
      </button>
      <h1 class="mt-3">Lenovo ThinkPad T14</h1>
      <p class="text-muted">Инвентарный номер: INV-0001</p>
    </div>
    <div class="row g-4">
      <div class="col-md-8">
        <div class="card shadow-sm mb-4">
          <div class="card-header">Основная информация</div>
          <div class="card-body">
            <div class="row mb-3">
              <div class="col-md-4 text-muted">Название</div>
              <div class="col-md-8">Lenovo ThinkPad T14</div>
            </div>
            <div class="row mb-3">
              <div class="col-md-4 text-muted">Инвентарный номер</div>
              <div class="col-md-8">INV-0001</div>
            </div>
            <div class="row mb-3">
              <div class="col-md-4 text-muted">Категория</div>
              <div class="col-md-8">Компьютерная техника</div>
            </div>
            <div class="row mb-3">
              <div class="col-md-4 text-muted">Дата поступления</div>
              <div class="col-md-8">15.03.2025</div>
            </div>
            <div class="row mb-3">
              <div class="col-md-4 text-muted">Состояние</div>
              <div class="col-md-8"><span class="badge text-bg-success"> Исправно </span></div>
            </div>
            <div class="row">
              <div class="col-md-4 text-muted">Статус</div>
              <div class="col-md-8"><span class="badge text-bg-success"> На складе </span></div>
            </div>
          </div>
        </div>
        <div class="card shadow-sm">
          <div class="card-header">История операций</div>
          <div class="card-body">
            <table class="table align-middle">
              <thead>
                <tr>
                  <th>Дата</th>
                  <th>Операция</th>
                  <th>Сотрудник</th>
                  <th>Комментарий</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>15.03.2025</td>
                  <td>Поступление</td>
                  <td>—</td>
                  <td>Первоначальная постановка на учёт</td>
                </tr>
                <tr>
                  <td>10.06.2025</td>
                  <td>Выдача</td>
                  <td>Иванов И.И.</td>
                  <td>Передано сотруднику</td>
                </tr>
                <tr>
                  <td>20.09.2026</td>
                  <td>Возврат</td>
                  <td>Иванов И.И.</td>
                  <td>Состояние: исправно</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card shadow-sm mb-4">
          <div class="card-header">Текущий ответственный</div>
          <div class="card-body">
            <h5>Не закреплено</h5>
            <p class="text-muted">Имущество находится на складе.</p>
          </div>
        </div>
        <div class="card shadow-sm">
          <div class="card-header">Действия</div>
          <div class="card-body d-grid gap-2">
            <button type="button" class="btn btn-primary" onclick="route('assetEdit')">Изменить</button>
            <button type="button" class="btn btn-outline-primary" onclick="route('issueCreate')">
              Оформить выдачу
            </button>
            <button type="button" class="btn btn-outline-danger">Списать имущество</button>
          </div>
        </div>
      </div>
    </div>
  `
}

export function assetCreatePage() {
  return `
    <div class="mb-4">
      <button type="button" class="btn btn-link text-decoration-none p-0" onclick="route('assets')">
        ← Назад к имуществу
      </button>
      <h1 class="mt-3">Добавление имущества</h1>
      <p class="text-muted">Добавление новой материальной ценности в систему</p>
    </div>
    <div class="row g-4">
      <div class="col-md-8">
        <div class="card shadow-sm">
          <div class="card-header">Основная информация</div>
          <div class="card-body">
            <form onsubmit="event.preventDefault(); route('assets')">
              <div class="mb-3">
                <label for="assetName" class="form-label"> Название </label>
                <input type="text" class="form-control" id="assetName" placeholder="Например, Lenovo ThinkPad T14" required />
              </div>
              <div class="mb-3">
                <label for="inventoryNumber" class="form-label"> Инвентарный номер </label>
                <input type="text" class="form-control" id="inventoryNumber" placeholder="Например, INV-0004" required />
                <div class="form-text">Инвентарный номер должен быть уникальным.</div>
              </div>
              <div class="mb-3">
                <label for="category" class="form-label"> Категория </label>
                <select class="form-select" id="category" required>
                  <option value="" selected disabled>Выберите категорию</option>
                  <option value="computer">Компьютерная техника</option>
                  <option value="furniture">Мебель</option>
                  <option value="office">Офисное оборудование</option>
                  <option value="other">Другое</option>
                </select>
              </div>
              <div class="mb-3">
                <label for="arrivalDate" class="form-label"> Дата поступления </label>
                <input type="date" class="form-control" id="arrivalDate" required />
              </div>
              <div class="mb-3">
                <label for="condition" class="form-label"> Состояние </label>
                <select class="form-select" id="condition" required>
                  <option value="" selected disabled>Выберите состояние</option>
                  <option value="good">Исправно</option>
                  <option value="repair">Требует ремонта</option>
                  <option value="broken">Неисправно</option>
                </select>
              </div>
              <div class="mb-4">
                <label for="comment" class="form-label"> Комментарий </label>
                <textarea class="form-control" id="comment" rows="4" placeholder="Дополнительная информация об имуществе"></textarea>
              </div>
              <div class="d-flex gap-2">
                <button type="submit" class="btn btn-primary">Добавить имущество</button>
                <button type="button" class="btn btn-outline-secondary" onclick="route('assets')">Отмена</button>
              </div>
            </form>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card shadow-sm">
          <div class="card-header">После добавления</div>
          <div class="card-body">
            <p class="mb-3">Новое имущество будет автоматически добавлено на склад.</p>
            <div class="mb-3">
              <div class="text-muted mb-1">Статус</div>
              <span class="badge text-bg-success"> На складе </span>
            </div>
            <div>
              <div class="text-muted mb-1">Ответственный</div>
              <div>Не закреплено</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  `
}

export function assetEditPage() {
  return `
    <div class="mb-4">
      <button type="button" class="btn btn-link text-decoration-none p-0" onclick="route('asset')">
        ← Назад к имуществу
      </button>
      <h1 class="mt-3">Изменение имущества</h1>
      <p class="text-muted">Редактирование информации об имуществе</p>
    </div>
    <div class="row g-4">
      <div class="col-md-8">
        <div class="card shadow-sm">
          <div class="card-header">Основная информация</div>
          <div class="card-body">
            <form onsubmit="event.preventDefault(); route('asset')">
              <div class="mb-3">
                <label for="assetName" class="form-label"> Название </label>
                <input type="text" class="form-control" id="assetName" value="Lenovo ThinkPad T14" required />
              </div>
              <div class="mb-3">
                <label for="inventoryNumber" class="form-label"> Инвентарный номер </label>
                <input type="text" class="form-control" id="inventoryNumber" value="INV-0001" readonly />
                <div class="form-text">Инвентарный номер нельзя изменить.</div>
              </div>
              <div class="mb-3">
                <label for="category" class="form-label"> Категория </label>
                <select class="form-select" id="category" required>
                  <option value="computer" selected>Компьютерная техника</option>
                  <option value="furniture">Мебель</option>
                  <option value="office">Офисное оборудование</option>
                  <option value="other">Другое</option>
                </select>
              </div>
              <div class="mb-3">
                <label for="arrivalDate" class="form-label"> Дата поступления </label>
                <input type="date" class="form-control" id="arrivalDate" value="2025-03-15" required />
              </div>
              <div class="mb-3">
                <label for="condition" class="form-label"> Состояние </label>
                <select class="form-select" id="condition" required>
                  <option value="good" selected>Исправно</option>
                  <option value="repair">Требует ремонта</option>
                  <option value="broken">Неисправно</option>
                </select>
              </div>
              <div class="mb-3">
                <label for="status" class="form-label"> Статус </label>
                <select class="form-select" id="status" required>
                  <option value="warehouse" selected>На складе</option>
                  <option value="issued">Выдано</option>
                  <option value="repair">На ремонте</option>
                  <option value="written-off">Списано</option>
                </select>
              </div>
              <div class="mb-4">
                <label for="comment" class="form-label"> Комментарий </label>
                <textarea class="form-control" id="comment" rows="4" placeholder="Дополнительная информация"></textarea>
              </div>
              <div class="d-flex gap-2">
                <button type="submit" class="btn btn-primary">Сохранить изменения</button>
                <button type="button" class="btn btn-outline-secondary" onclick="route('asset')">Отмена</button>
              </div>
            </form>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card shadow-sm mb-4">
          <div class="card-header">Текущий ответственный</div>
          <div class="card-body">
            <h5>Не закреплено</h5>
            <p class="text-muted mb-0">Имущество находится на складе.</p>
          </div>
        </div>
        <div class="card shadow-sm">
          <div class="card-header">Информация</div>
          <div class="card-body">
            <p class="mb-0 text-muted">
              После сохранения изменений обновлённые данные будут отображаться в карточке имущества.
            </p>
          </div>
        </div>
      </div>
    </div>
  `
}
