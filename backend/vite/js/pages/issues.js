export function issuesPage() {
  return `
    <div class="d-flex justify-content-between align-items-center mb-4">
      <div>
        <h1>Выдачи имущества</h1>
        <p class="text-muted mb-0">История и управление выдачей материальных ценностей</p>
      </div>
      <button type="button" class="btn btn-primary" onclick="route('issueCreate')">
        + Оформить выдачу
      </button>
    </div>
    <div class="card shadow-sm mb-4">
      <div class="card-body">
        <div class="row g-3">
          <div class="col-md-3">
            <label class="form-label"> Сотрудник </label>
            <select class="form-select">
              <option selected>Все сотрудники</option>
              <option>Иванов И.И.</option>
              <option>Петров П.П.</option>
              <option>Сидоров А.С.</option>
            </select>
          </div>
          <div class="col-md-3">
            <label class="form-label"> Статус </label>
            <select class="form-select">
              <option selected>Все</option>
              <option>Выдано</option>
              <option>Возвращено</option>
            </select>
          </div>
          <div class="col-md-2">
            <label class="form-label"> С даты </label>
            <input type="date" class="form-control" />
          </div>
          <div class="col-md-2">
            <label class="form-label"> По дату </label>
            <input type="date" class="form-control" />
          </div>
          <div class="col-md-2 d-flex align-items-end">
            <button class="btn btn-primary w-100">Применить</button>
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
                <th>ID</th>
                <th>Дата выдачи</th>
                <th>Сотрудник</th>
                <th>Имущество</th>
                <th>Плановый возврат</th>
                <th>Фактический возврат</th>
                <th>Статус</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>#0001</td>
                <td>10.06.2025</td>
                <td>Иванов И.И.</td>
                <td>Dell UltraSharp</td>
                <td>10.06.2026</td>
                <td>—</td>
                <td><span class="badge text-bg-primary"> Выдано </span></td>
                <td>
                  <button type="button" class="btn btn-sm btn-outline-success" onclick="route('returnCreate')">
                    Возврат
                  </button>
                </td>
              </tr>
              <tr>
                <td>#0002</td>
                <td>12.06.2025</td>
                <td>Петров П.П.</td>
                <td>HP ProBook</td>
                <td>12.06.2026</td>
                <td>20.09.2026</td>
                <td><span class="badge text-bg-success"> Возвращено </span></td>
                <td>
                  <button class="btn btn-sm btn-outline-secondary">Просмотр</button>
                </td>
              </tr>
              <tr>
                <td>#0003</td>
                <td>25.09.2026</td>
                <td>Сидоров А.С.</td>
                <td>Logitech MX Keys</td>
                <td>25.09.2027</td>
                <td>—</td>
                <td><span class="badge text-bg-primary"> Выдано </span></td>
                <td>
                  <button type="button" class="btn btn-sm btn-outline-success" onclick="route('returnCreate')">
                    Возврат
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  `
}

export function issueCreatePage() {
  return `
    <div class="mb-4">
      <button type="button" class="btn btn-link text-decoration-none p-0" onclick="route('issues')">
        ← Назад к выдачам
      </button>
      <h1 class="mt-3">Оформление выдачи</h1>
      <p class="text-muted">Передача материальной ценности сотруднику</p>
    </div>
    <div class="row">
      <div class="col-lg-8">
        <div class="card shadow-sm">
          <div class="card-header">Данные выдачи</div>
          <div class="card-body">
            <form onsubmit="event.preventDefault(); route('issues')">
              <div class="mb-3">
                <label class="form-label"> Сотрудник </label>
                <select class="form-select">
                  <option selected>Выберите сотрудника</option>
                  <option>Иванов Иван Иванович</option>
                  <option>Петров Пётр Петрович</option>
                  <option>Сидоров Алексей Сергеевич</option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label"> Материальная ценность </label>
                <select class="form-select">
                  <option selected>Выберите имущество</option>
                  <option>INV-0001 — Lenovo ThinkPad T14</option>
                  <option>INV-0006 — HP ProBook</option>
                  <option>INV-0007 — Logitech MX Keys</option>
                </select>
                <div class="form-text">Отображается только доступное имущество.</div>
              </div>
              <div class="row">
                <div class="col-md-6 mb-3">
                  <label class="form-label"> Дата выдачи </label>
                  <input type="date" class="form-control" value="2026-09-27" />
                </div>
                <div class="col-md-6 mb-3">
                  <label class="form-label"> Планируемая дата возврата </label>
                  <input type="date" class="form-control" />
                </div>
              </div>
              <div class="mb-4">
                <label class="form-label"> Подробное состояние </label>
                <textarea class="form-control" rows="4" placeholder="Дополнительная информация"></textarea>
              </div>
              <div class="mb-4">
                <label class="form-label"> Комментарий </label>
                <textarea class="form-control" rows="4" placeholder="Дополнительная информация"></textarea>
              </div>
              <div class="d-flex gap-2">
                <button type="submit" class="btn btn-primary">Оформить выдачу</button>
                <button type="button" class="btn btn-outline-secondary" onclick="route('issues')">Отмена</button>
              </div>
            </form>
          </div>
        </div>
      </div>
      <div class="col-lg-4">
        <div class="card shadow-sm">
          <div class="card-header">Информация</div>
          <div class="card-body">
            <p>После оформления выдачи:</p>
            <ul>
              <li>имущество получает статус «Выдано»;</li>
              <li>имущество закрепляется за сотрудником;</li>
              <li>операция добавляется в историю;</li>
              <li>создаётся запись о выдаче.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  `
}

export function returnCreatePage() {
  return `
    <div class="mb-4">
      <button type="button" class="btn btn-link text-decoration-none p-0" onclick="route('issues')">
        ← Назад к выдачам
      </button>
      <h1 class="mt-3">Оформление возврата</h1>
      <p class="text-muted">Возврат материальной ценности от сотрудника</p>
    </div>
    <div class="row">
      <div class="col-lg-8">
        <div class="card shadow-sm">
          <div class="card-header">Данные возврата</div>
          <div class="card-body">
            <form onsubmit="event.preventDefault(); route('issues')">
              <div class="mb-3">
                <label class="form-label"> Сотрудник </label>
                <select class="form-select">
                  <option selected>Иванов Иван Иванович</option>
                  <option>Петров Пётр Петрович</option>
                  <option>Сидоров Алексей Сергеевич</option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label"> Материальная ценность </label>
                <select class="form-select">
                  <option selected>INV-0002 — Dell UltraSharp</option>
                  <option>INV-0005 — HP ProBook</option>
                </select>
              </div>
              <div class="mb-3">
                <label class="form-label"> Дата возврата </label>
                <input type="date" class="form-control" value="2026-09-27" />
              </div>
              <div class="mb-3">
                <label class="form-label"> Состояние при возврате </label>
                <select class="form-select">
                  <option selected>Исправно</option>
                  <option>Повреждено</option>
                  <option>Требует ремонта</option>
                </select>
              </div>
              <div class="mb-4">
                <label class="form-label"> Комментарий </label>
                <textarea class="form-control" rows="4" placeholder="Укажите состояние имущества или замечания"></textarea>
              </div>
              <div class="d-flex gap-2">
                <button type="submit" class="btn btn-success">Оформить возврат</button>
                <button type="button" class="btn btn-outline-secondary" onclick="route('issues')">Отмена</button>
              </div>
            </form>
          </div>
        </div>
      </div>
      <div class="col-lg-4">
        <div class="card shadow-sm">
          <div class="card-header">После возврата</div>
          <div class="card-body">
            <ul>
              <li>статус имущества изменяется;</li>
              <li>имущество снимается с подотчёта сотрудника;</li>
              <li>фиксируется состояние имущества;</li>
              <li>операция записывается в историю.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  `
}
