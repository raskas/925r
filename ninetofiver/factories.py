import random
import factory
from faker import Faker
from django.contrib.auth import models as auth_models
from django.utils.timezone import utc
from ninetofiver import models


fake = Faker()


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = auth_models.User

    first_name = factory.LazyFunction(fake.first_name)
    last_name = factory.LazyFunction(fake.last_name)
    username = factory.LazyFunction(fake.name)
    is_staff = False


class AdminFactory(UserFactory):
    is_staff = True


class CompanyFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Company

    name = factory.LazyFunction(fake.company)
    country = factory.LazyFunction(fake.country_code)
    vat_identification_number = factory.LazyFunction(lambda: '%s%s' % (fake.language_code(), fake.md5()[:10]))
    internal = factory.LazyFunction(fake.boolean)
    address = factory.LazyFunction(fake.address)


class InternalCompanyFactory(CompanyFactory):
    internal = True


class EmploymentContractFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.EmploymentContract

    started_at = factory.LazyFunction(lambda: fake.date_time_this_decade(before_now=True))
    ended_at = factory.LazyFunction(lambda: fake.date_time_this_decade(after_now=True))


class WorkScheduleFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.WorkSchedule

    label = factory.LazyFunction(fake.word)
    monday = factory.LazyFunction(lambda: random.randint(0, 24))
    tuesday = factory.LazyFunction(lambda: random.randint(0, 24))
    wednesday = factory.LazyFunction(lambda: random.randint(0, 24))
    thursday = factory.LazyFunction(lambda: random.randint(0, 24))
    friday = factory.LazyFunction(lambda: random.randint(0, 24))
    saturday = factory.LazyFunction(lambda: random.randint(0, 24))
    sunday = factory.LazyFunction(lambda: random.randint(0, 24))


class UserRelativeFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.UserRelative

    name = factory.LazyFunction(fake.name)
    birth_date = factory.LazyFunction(lambda: fake.date_time_this_decade(before_now=True))
    gender = factory.LazyFunction(lambda: fake.simple_profile(sex=None)['sex'])
    relation = factory.LazyFunction(fake.word)


class HolidayFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Holiday

    name = factory.LazyFunction(fake.word)
    date = factory.LazyFunction(lambda: fake.date_time_this_decade(before_now=True))
    country = factory.LazyFunction(fake.country_code)


class LeaveTypeFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.LeaveType

    label = factory.LazyFunction(fake.word)


class LeaveFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Leave

    description = factory.LazyFunction(lambda: fake.text(max_nb_chars=200))


class LeaveDateFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.LeaveDate

    starts_at = factory.LazyFunction(lambda: fake.date_time_between(start_date='-1h', end_date='now', tzinfo=utc))
    ends_at = factory.LazyFunction(lambda: fake.date_time_between(start_date='now', end_date='+1h', tzinfo=utc))


class PerformanceTypeFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.PerformanceType

    label = factory.LazyFunction(fake.word)
    description = factory.LazyFunction(lambda: fake.text(max_nb_chars=200))
    multiplier = factory.LazyFunction(lambda: random.randint(0, 3))


class ContractFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Contract

    label = factory.LazyFunction(fake.word)
    description = factory.LazyFunction(lambda: fake.text(max_nb_chars=200))
    active = factory.LazyFunction(fake.boolean)


class ContractRoleFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.ContractRole

    label = factory.LazyFunction(fake.word)
    description = factory.LazyFunction(lambda: fake.text(max_nb_chars=200))


class ContractUserFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.ContractUser


class TimesheetFactory(factory.DjangoModelFactory):
    class Meta:
        model = models.Timesheet

    year = factory.LazyFunction(lambda: random.randint(2000, 3000))
    month = factory.LazyFunction(lambda: random.randint(1, 12))
    closed = factory.LazyFunction(fake.boolean)
