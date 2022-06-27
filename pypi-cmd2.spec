#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cmd2
Version  : 2.4.1
Release  : 118
URL      : https://files.pythonhosted.org/packages/0b/22/3206860cce08a384909fdf7f7bf21a20d881c6ce533f0b046bb356a373ef/cmd2-2.4.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/0b/22/3206860cce08a384909fdf7f7bf21a20d881c6ce533f0b046bb356a373ef/cmd2-2.4.1.tar.gz
Summary  : A tool for building interactive command line apps
Group    : Development/Tools
License  : MIT
Requires: pypi-cmd2-license = %{version}-%{release}
Requires: pypi-cmd2-python = %{version}-%{release}
Requires: pypi-cmd2-python3 = %{version}-%{release}
Requires: which
BuildRequires : buildreq-distutils3
BuildRequires : pypi(attrs)
BuildRequires : pypi(pyperclip)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(wcwidth)
BuildRequires : pypi(wheel)

%description
cmd2 is a tool for building interactive command line applications in Python.
Its goal is to make it quick and easy for developers to build feature-rich and
user-friendly interactive command line applications. It provides a simple API
which is an extension of Python's built-in cmd module. cmd2 provides a wealth
of features on top of cmd to make your life easier and eliminates much of the
boilerplate code which would be necessary when using cmd.

%package license
Summary: license components for the pypi-cmd2 package.
Group: Default

%description license
license components for the pypi-cmd2 package.


%package python
Summary: python components for the pypi-cmd2 package.
Group: Default
Requires: pypi-cmd2-python3 = %{version}-%{release}

%description python
python components for the pypi-cmd2 package.


%package python3
Summary: python3 components for the pypi-cmd2 package.
Group: Default
Requires: python3-core
Provides: pypi(cmd2)
Requires: pypi(attrs)
Requires: pypi(pyperclip)
Requires: pypi(wcwidth)

%description python3
python3 components for the pypi-cmd2 package.


%prep
%setup -q -n cmd2-2.4.1
cd %{_builddir}/cmd2-2.4.1
pushd ..
cp -a cmd2-2.4.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656366075
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cmd2
cp %{_builddir}/cmd2-2.4.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cmd2/b2e34f088b600127f76aa6629d3d43f3179e8fe5
cp %{_builddir}/cmd2-2.4.1/plugins/template/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cmd2/3e6eb52ad8a3906e168e16d4a635f441ff29e02b
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cmd2/3e6eb52ad8a3906e168e16d4a635f441ff29e02b
/usr/share/package-licenses/pypi-cmd2/b2e34f088b600127f76aa6629d3d43f3179e8fe5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
